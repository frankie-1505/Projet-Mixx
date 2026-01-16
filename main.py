import sys
import json
import hashlib
from pathlib import Path
from datetime import datetime
from typing import List, Optional

from PyQt5.QtCore import QObject, pyqtSlot, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel

from models.partner import Partner
from models.transaction import Transaction, TransactionState
from models.recap_config import RecapConfig, ConditionReglement
from utils.formatters import format_currency, format_date


class Bridge(QObject):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.partners: List[Partner] = []
        self.transactions: List[Transaction] = []
        self.recap_config: Optional[RecapConfig] = None
        self.pin_hash = self.load_pin()

    def load_pin(self) -> str:
        """Charge le PIN depuis le fichier ou crée un PIN par défaut (0000)"""
        pin_file = Path("data/pin.txt")
        if pin_file.exists():
            return pin_file.read_text().strip()
        else:
            pin_file.parent.mkdir(parents=True, exist_ok=True)
            default_pin = hashlib.sha256("0000".encode()).hexdigest()
            pin_file.write_text(default_pin)
            return default_pin

    def save_pin(self, pin_hash: str):
        """Sauvegarde le hash du PIN"""
        pin_file = Path("data/pin.txt")
        pin_file.parent.mkdir(parents=True, exist_ok=True)
        pin_file.write_text(pin_hash)
        self.pin_hash = pin_hash

    def load_partners(self) -> List[Partner]:
        """Charge les partenaires depuis le fichier JSON"""
        partners_file = Path("data/partners.json")
        if partners_file.exists():
            with open(partners_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Partner(**p) for p in data]
        return []

    def save_partners(self):
        """Sauvegarde les partenaires dans le fichier JSON"""
        partners_file = Path("data/partners.json")
        partners_file.parent.mkdir(parents=True, exist_ok=True)
        data = [{"id": p.id, "nom": p.nom, "alias": p.alias, "services": getattr(p, 'services', []),
                 "commission": getattr(p, 'commission', 0), "retenue": getattr(p, 'retenue', 0),
                 "tva": getattr(p, 'tva', 18)} for p in self.partners]
        with open(partners_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @pyqtSlot()
    def traiterEtats(self):
        self.main_window.load_page("import.html")

    @pyqtSlot()
    def configurations(self):
        self.main_window.load_page("config.html")

    @pyqtSlot()
    def goBack(self):
        self.main_window.load_page("home.html")

    @pyqtSlot(str)
    def verifyPin(self, pin: str):
        pin_hash = hashlib.sha256(pin.encode()).hexdigest()
        success = pin_hash == self.pin_hash
        self.main_window.web_view.page().runJavaScript(f"onPinVerified({str(success).lower()})")
        if success:
            self.partners = self.load_partners()

    @pyqtSlot()
    def getPartners(self):
        partners_data = []
        for p in self.partners:
            partners_data.append({
                "id": p.id,
                "nom": p.nom,
                "alias": p.alias,
                "services": getattr(p, 'services', []),
                "commission": getattr(p, 'commission', 0),
                "retenue": getattr(p, 'retenue', 0),
                "tva": getattr(p, 'tva', 18)
            })
        json_data = json.dumps(partners_data, ensure_ascii=False)
        self.main_window.web_view.page().runJavaScript(f"updatePartnersTable('{json_data}')")

    @pyqtSlot(str)
    def addPartner(self, data_json: str):
        data = json.loads(data_json)
        new_id = str(max([int(p.id) for p in self.partners], default=0) + 1)
        
        partner = Partner(
            id=new_id,
            nom=data['nom'],
            alias=data.get('alias', '')
        )
        partner.services = data.get('services', [])
        partner.commission = data.get('commission', 0)
        partner.retenue = data.get('retenue', 0)
        partner.tva = data.get('tva', 18)
        
        self.partners.append(partner)
        self.save_partners()
        self.getPartners()

    @pyqtSlot(str)
    def updatePartner(self, data_json: str):
        data = json.loads(data_json)
        partner = next((p for p in self.partners if p.id == str(data['id'])), None)
        if partner:
            partner.nom = data['nom']
            partner.alias = data.get('alias', '')
            partner.services = data.get('services', [])
            partner.commission = data.get('commission', 0)
            partner.retenue = data.get('retenue', 0)
            partner.tva = data.get('tva', 18)
            self.save_partners()
            self.getPartners()

    @pyqtSlot(str)
    def deletePartner(self, partner_id: str):
        self.partners = [p for p in self.partners if p.id != partner_id]
        self.save_partners()
        self.getPartners()

    @pyqtSlot(str, str)
    def changePIN(self, current_pin: str, new_pin: str):
        current_hash = hashlib.sha256(current_pin.encode()).hexdigest()
        if current_hash == self.pin_hash:
            new_hash = hashlib.sha256(new_pin.encode()).hexdigest()
            self.save_pin(new_hash)
            self.main_window.web_view.page().runJavaScript("onPinChanged(true)")
        else:
            self.main_window.web_view.page().runJavaScript("onPinChanged(false)")

    @pyqtSlot()
    def selectFile(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.main_window,
            "Sélectionner un fichier Excel",
            "",
            "Excel Files (*.xlsx *.xls)"
        )
        if file_path:
            self.main_window.web_view.page().runJavaScript(f"setFilePath('{file_path}')")

    @pyqtSlot(str)
    def submitForm(self, form_data_json: str):
        try:
            data = json.loads(form_data_json)
            
            self.recap_config = RecapConfig(
                titre=data['titre'],
                condition_reglement=ConditionReglement[data['conditionReglement']],
                mode_paiement=data['modePaiement'],
                excel_path=data['fichierExcel']
            )
            
            # Simuler le chargement des transactions depuis Excel
            # Dans la vraie version, vous utiliseriez pandas ou openpyxl
            self.transactions = self.load_transactions_from_excel(data['fichierExcel'])
            
            # Charger la page de traitement
            self.main_window.load_page("processing.html")
            self.send_processing_data()
            
        except Exception as e:
            self.main_window.web_view.page().runJavaScript("hideLoader()")
            QMessageBox.critical(self.main_window, "Erreur", f"Erreur lors du traitement: {str(e)}")

    def load_transactions_from_excel(self, excel_path: str) -> List[Transaction]:
        """Charge les transactions depuis le fichier Excel"""
        # Cette fonction devrait lire le fichier Excel et créer des objets Transaction
        # Pour l'instant, retournons des données de test
        from datetime import date
        
        return [
            Transaction(
                id="1",
                nom="PARTENAIRE TEST 1",
                date_debut=date(2024, 1, 1),
                date_fin=date(2024, 1, 31),
                montant_trans=1000000,
                montant_reverse=950000,
                commission=50000,
                alias="PT1"
            ),
            Transaction(
                id="2",
                nom="PARTENAIRE TEST 2",
                date_debut=date(2024, 1, 1),
                date_fin=date(2024, 1, 31),
                montant_trans=500000,
                montant_reverse=500000,
                alias="PT2"
            )
        ]

    def send_processing_data(self):
        """Envoie les données à la page de traitement"""
        transactions_data = []
        for t in self.transactions:
            transactions_data.append({
                "id": t.id,
                "nom": t.nom,
                "alias": t.alias,
                "date_debut": format_date(t.date_debut),
                "date_fin": format_date(t.date_fin),
                "montant_trans": t.montant_trans,
                "montant_reverse": t.montant_reverse,
                "commission": t.commission,
                "agregation": t.agregation,
                "annulation": t.annulation
            })

        partners_data = []
        for p in self.partners:
            partners_data.append({
                "id": p.id,
                "nom": p.nom,
                "alias": p.alias,
                "services": getattr(p, 'services', [])
            })

        data = {
            "title": self.recap_config.titre if self.recap_config else "Récapitulatif",
            "transactions": transactions_data,
            "partners": partners_data
        }

        json_data = json.dumps(data, ensure_ascii=False)
        json_escaped = json_data.replace("'", "\\'").replace('"', '\\"')
        self.main_window.web_view.page().runJavaScript(f'initData("{json_escaped}")')

    @pyqtSlot(str)
    def remboursement(self, transaction_id: str):
        transaction = next((t for t in self.transactions if t.id == transaction_id), None)
        if transaction:
            transaction.mark_remboursement_done()
            print(f"État de reversement validé pour transaction {transaction_id}")

    @pyqtSlot(str)
    def commission(self, transaction_id: str):
        transaction = next((t for t in self.transactions if t.id == transaction_id), None)
        if transaction:
            transaction.mark_commission_done()
            print(f"État de commission validé pour transaction {transaction_id}")

    @pyqtSlot(str)
    def dtrf(self, transaction_id: str):
        print(f"DTRF pour transaction {transaction_id}")

    @pyqtSlot(str)
    def pigual(self, transaction_id: str):
        print(f"PIGUAL pour transaction {transaction_id}")

    @pyqtSlot()
    def generatePDF(self):
        """Génère les PDFs pour toutes les transactions traitées"""
        try:
            # Simuler la génération de PDF
            import time
            time.sleep(2)  # Simuler un délai de traitement
            
            self.main_window.web_view.page().runJavaScript("onPDFGenerated()")
        except Exception as e:
            QMessageBox.critical(self.main_window, "Erreur", f"Erreur lors de la génération des PDF: {str(e)}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("iFacturier Plus")
        self.setGeometry(100, 100, 1400, 900)

        # Configuration du WebView
        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)

        # Configuration du WebChannel
        self.channel = QWebChannel()
        self.bridge = Bridge(self)
        self.channel.registerObject('bridge', self.bridge)
        self.web_view.page().setWebChannel(self.channel)

        # Charger la page d'accueil
        self.load_page("home.html")

    def load_page(self, page_name: str):
        """Charge une page HTML"""
        html_path = Path("html") / page_name
        if html_path.exists():
            url = QUrl.fromLocalFile(str(html_path.absolute()))
            self.web_view.setUrl(url)
        else:
            QMessageBox.critical(self, "Erreur", f"Page {page_name} introuvable")


def main():
    # Dossiers de base
    for d in ["data", "html", "output"]:
        Path(d).mkdir(exist_ok=True)

    # AJOUTEZ CES DEUX LIGNES ICI :
    from PyQt5.QtCore import Qt
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts) 

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
