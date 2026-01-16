# ProjetMixxByYasIfacturier

<body>
    <div class="container">
        <div class="header-bar">
            <h1 class="header-title">TRAITEMENT DES ETATS MIXX BY YAS</h1>
            <button class="btn-back" onclick="goBack()">← Retour</button>
        </div>
        <div class="split-view">
            <div class="panel">
                <div class="panel-header">
                    <h3 id="recapTitle"></h3>
                </div>
                <div class="table-container">
                    <table>
                        <thead id="tableHead">
                        </thead>
                        <tbody id="tableBody"></tbody>
                    </table>
                </div>
            </div>

            <div class="panel">
                <div class="panel-header">
                    <h3>Transactions</h3>
                    <div class="dropdown" id="actionsDropdown">
                        <button class="dropdown-btn" onclick="toggleDropdown()">
                            Actions Rapides
                            <span>▾</span>
                        </button>
                        <div class="dropdown-menu">
                            <div class="dropdown-item" id="actionBulkReversement" onclick="handleBulkReversement()">
                                Valider tous les états de reversement
                            </div>
                            <div class="dropdown-item" id="actionBulkCommission" onclick="handleBulkCommission()">
                                Valider tous les états de commissions
                            </div>
                        </div>
                    </div>
                </div>
                <div class="cards-container" id="cardsContainer"></div>
            </div>
        </div>

        <div class="footer">
            <div class="footer-info">
                <strong id="completedCount">0</strong> transaction(s) traitée(s) sur <strong id="totalCount">0</strong>
            </div>
            <button class="btn-generate" id="generateBtn" disabled onclick="generatePDF()">
                Générer les PDF de toutes les transactions traitées
            </button>
        </div>
    </div>

    <!-- Modal DTRF -->
    <div class="modal-overlay" id="modalDTRF">
        <div class="modal-content">
            <div class="modal-header">
                <h2 class="modal-title">ÉTAT DTRF (IMMATRICULATION)</h2>
                <button class="modal-close" onclick="closeModal('modalDTRF')">&times;</button>
            </div>
            <div class="modal-body">
                <form id="formDTRF" onsubmit="submitDTRF(event)">
                    <div class="form-grid">
                        <div class="form-group">
                            <label class="form-label">Numéro de dossier</label>
                            <input type="text" class="form-input" name="numero_dossier" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Date de réception</label>
                            <input type="date" class="form-input" name="date_reception" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Nom du demandeur</label>
                            <input type="text" class="form-input" name="nom_demandeur" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Type de véhicule</label>
                            <input type="text" class="form-input" name="type_vehicule">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Numéro d'immatriculation</label>
                            <input type="text" class="form-input" name="numero_immatriculation">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Montant des frais</label>
                            <input type="number" step="0.01" class="form-input" name="montant_frais">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Statut du dossier</label>
                            <input type="text" class="form-input" name="statut_dossier">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Agent traitant</label>
                            <input type="text" class="form-input" name="agent_traitant">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Observations</label>
                            <input type="text" class="form-input" name="observations">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Date de traitement</label>
                            <input type="date" class="form-input" name="date_traitement">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="modal-btn modal-btn-cancel" onclick="closeModal('modalDTRF')">Annuler</button>
                        <button type="submit" class="modal-btn modal-btn-submit">Valider</button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <!-- Modal Success -->
    <div class="modal-overlay confirm-modal" id="modalSuccess">
        <div class="modal-content">
            <div class="modal-header"></div>
            <div class="modal-body">
                <div class="modal-icon" id="successIcon">✓</div>
                <h2 class="modal-title" id="successTitle">Succès</h2>
                <div class="modal-message" id="successMessage"></div>
            </div>
            <div class="modal-footer">
                <button class="modal-btn-submit" onclick="closeModal('modalSuccess')">OK</button>
            </div>
        </div>
    </div>

    <!-- Modal PIGUAL -->
    <div class="modal-overlay" id="modalPigual">
        <div class="modal-content">
            <div class="modal-header">
                <h2 class="modal-title">ÉTAT PIGUAL</h2>
                <button class="modal-close" onclick="closeModal('modalPigual')">&times;</button>
            </div>
            <div class="modal-body">
                <form id="formPigual" onsubmit="submitPigual(event)">
                    <div class="form-grid">
                        <div class="form-group">
                            <label class="form-label">Référence</label>
                            <input type="text" class="form-input" name="reference" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Date de demande</label>
                            <input type="date" class="form-input" name="date_demande" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Nom du client</label>
                            <input type="text" class="form-input" name="nom_client" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Montant TTC</label>
                            <input type="number" step="0.01" class="form-input" name="montant_ttc">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Type de prestation</label>
                            <input type="text" class="form-input" name="type_prestation">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Mode de paiement</label>
                            <input type="text" class="form-input" name="mode_paiement">
                        </div>
                        <div class="form-group">
                            <label class="form-label">État d'avancement</label>
                            <input type="text" class="form-input" name="etat_avancement">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Date de clôture</label>
                            <input type="date" class="form-input" name="date_cloture">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Remarques</label>
                            <input type="text" class="form-input" name="remarques">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Validé par</label>
                            <input type="text" class="form-input" name="valide_par">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="modal-btn modal-btn-cancel" onclick="closeModal('modalPigual')">Annuler</button>
                        <button type="submit" class="modal-btn modal-btn-submit">Valider</button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <!-- Modal Confirmation Retour -->
    <div class="modal-overlay confirm-modal" id="modalConfirmBack">
        <div class="modal-content">
            <div class="modal-header">
                <button class="modal-close" onclick="closeModal('modalConfirmBack')">&times;</button>
            </div>
            <div class="modal-body">
                <div class="modal-icon">⚠️</div>
                <h2 class="modal-title">Quitter le traitement</h2>
                <div class="modal-message">
                    Toutes les données saisies et le traitement en cours seront perdus.
                </div>
            </div>
            <div class="modal-footer">
                <button class="modal-btn-cancel" onclick="closeModal('modalConfirmBack')">Annuler</button>
                <button class="modal-btn-submit" onclick="confirmGoBack()">Quitter</button>
            </div>
        </div>
    </div>

    <!-- Modal Confirmation PDF Généré -->
    <div class="modal-overlay confirm-modal" id="modalPDFGenerated">
        <div class="modal-content">
            <div class="modal-header"></div>
            <div class="modal-body">
                <div class="modal-icon">✅</div>
                <h2 class="modal-title">PDF générés avec succès</h2>
                <div class="modal-message">
                    Les documents PDF ont été générés et enregistrés.<br>Voulez-vous retourner à la page d'accueil ?
                </div>
            </div>
            <div class="modal-footer">
                <button class="modal-btn-cancel" onclick="closeModal('modalPDFGenerated')">Non</button>
                <button class="modal-btn-submit" onclick="confirmReturnHome()">Oui</button>
            </div>
        </div>
    </div>

    <!-- Modal Confirmation Bulk Reversement -->
    <div class="modal-overlay confirm-modal" id="modalBulkReversement">
        <div class="modal-content">
            <div class="modal-header"></div>
            <div class="modal-body">
                <div class="modal-icon">⚡</div>
                <h2 class="modal-title">Validation en masse</h2>
                <div class="modal-message" id="bulkReversementMessage"></div>
            </div>
            <div class="modal-footer">
                <button class="modal-btn-cancel" onclick="closeModal('modalBulkReversement')">Annuler</button>
                <button class="modal-btn-submit" onclick="confirmBulkReversement()">Valider</button>
            </div>
        </div>
    </div>

    <!-- Modal Confirmation Bulk Commission -->
    <div class="modal-overlay confirm-modal" id="modalBulkCommission">
        <div class="modal-content">
            <div class="modal-header"></div>
            <div class="modal-body">
                <div class="modal-icon">⚡</div>
                <h2 class="modal-title">Validation en masse</h2>
                <div class="modal-message" id="bulkCommissionMessage"></div>
            </div>
            <div class="modal-footer">
                <button class="modal-btn-cancel" onclick="closeModal('modalBulkCommission')">Annuler</button>
                <button class="modal-btn-submit" onclick="confirmBulkCommission()">Valider</button>
            </div>
        </div>
    </div>

    <div class="loader-overlay" id="loader">
        <div class="loader-content">
            <div class="spinner"></div>
            <div class="loader-text">Génération des PDF en cours...</div>
        </div>
    </div>

    <script src="qrc:///qtwebchannel/qwebchannel.js"></script>
    <script>
        let bridge;
        let transactions = [];
        let partners = [];
        let transactionStates = {};

        new QWebChannel(qt.webChannelTransport, function(channel) {
            bridge = channel.objects.bridge;
        });

        function goBack() {
            openModal('modalConfirmBack');
        }

        function confirmGoBack() {
            closeModal('modalConfirmBack');
            if (bridge) {
                bridge.goBack();
            }
        }

        function initData(data) {
            const parsed = JSON.parse(data);
            document.getElementById('recapTitle').textContent = parsed.title;
            transactions = parsed.transactions;
            partners = parsed.partners;

            transactions.forEach(t => {
                transactionStates[t.id] = { remboursement: false, commission: false };
            });

            renderTable();
            renderCards();
            updateFooter();
            updateActionsDropdown();
        }

        function renderTable() {
            const hasCommission = transactions.some(t => t.commission > 0);
            const thead = document.getElementById('tableHead');
            const tbody = document.getElementById('tableBody');

            if (hasCommission) {
                thead.innerHTML = `
                    <tr>
                        <th>IDENTIFIANT</th>
                        <th>ALIAS</th>
                        <th>NOM</th>
                        <th>DEBUT_PERIODE</th>
                        <th>FIN_PERIODE</th>
                        <th>MONTANT TRANS</th>
                        <th>AGREGATION</th>
                        <th>ANNULATION</th>
                        <th>COMMISSION</th>
                        <th>MONTANT A REVERSE</th>
                    </tr>
                `;
                tbody.innerHTML = transactions.map(t => `
                    <tr>
                        <td>${t.id}</td>
                        <td>${t.alias || '-'}</td>
                        <td>${t.nom}</td>
                        <td>${t.date_debut}</td>
                        <td>${t.date_fin}</td>
                        <td>${formatNumber(t.montant_trans)}</td>
                        <td>${t.agregation || '-'}</td>
                        <td>${t.annulation || '-'}</td>
                        <td>${t.commission ? formatNumber(t.commission) : '-'}</td>
                        <td>${formatNumber(t.montant_reverse)}</td>
                    </tr>
                `).join('');
            } else {
                thead.innerHTML = `
                    <tr>
                        <th>NUMEROS</th>
                        <th>SHORT_CODE</th>
                        <th>NOM</th>
                        <th>PERIODE_DEBUT</th>
                        <th>PERIODE_FIN</th>
                        <th>MONTANT_TOTAL</th>
                        <th>ANNULATION</th>
                        <th>MONTANT_A_REVERSE</th>
                    </tr>
                `;
                tbody.innerHTML = transactions.map(t => `
                    <tr>
                        <td>${t.id}</td>
                        <td>${t.alias || '-'}</td>
                        <td>${t.nom}</td>
                        <td>${t.date_debut}</td>
                        <td>${t.date_fin}</td>
                        <td>${formatNumber(t.montant_trans)}</td>
                        <td>${t.annulation || '-'}</td>
                        <td>${formatNumber(t.montant_reverse)}</td>
                    </tr>
                `).join('');
            }
        }

        function renderCards() {
            const container = document.getElementById('cardsContainer');
            container.innerHTML = transactions.map(t => createCard(t)).join('');

            transactions.forEach(t => {
                const partnerSelect = document.getElementById(`partner-${t.id}`);
                if (partnerSelect && partnerSelect.selectedIndex > 0) {
                    const selectedValue = partnerSelect.value;
                    if (selectedValue && !selectedValue.includes('⚠️') && !selectedValue.includes('────') && selectedValue !== '-- Sélectionner --') {
                        updateServices(t.id);
                    }
                }
            });
        }

        function createCard(t) {
            const matches = findPartnerMatches(t.nom);
            const partnerOptions = buildPartnerOptions(matches);

            return `
                <div class="transaction-card" id="card-${t.id}">
                    <div class="card-name">${t.nom} (${t.date_debut} - ${t.date_fin})</div>
                    <div class="card-cols">
                        <div class="card-left">
                            <div class="amount-text">Montant à reverser : ${formatCurrency(t.montant_reverse)}</div>
                            ${t.commission > 0 ? `<div class="commission-text">Commission : ${formatCurrency(t.commission)}</div>` : ''}
                            <input type="text" placeholder="🔍 Barre de recherche..." oninput="filterPartners('${t.id}', this.value)">
                            <select id="partner-${t.id}" onchange="updateServices('${t.id}')">${partnerOptions}</select>
                            <select id="service-${t.id}">
                                <option selected>COLLECTE DE PAIEMENTS</option>
                            </select>
                        </div>
                        <div class="card-right">
                            <button class="btn" id="btn-reversement-${t.id}" onclick="handleRemboursement('${t.id}')">ÉTAT DE REVERSEMENT</button>
                            ${t.commission > 0 ? `<button class="btn" id="btn-commission-${t.id}" onclick="handleCommission('${t.id}')">ÉTAT DE COMMISSION</button>` : ''}
                            <button class="btn btn-blue" disabled title="Fonctionnalité à venir">ETAT DTRF (IMMATRICULATION)</button>
                            <button class="btn btn-blue" disabled title="Fonctionnalité à venir">ETAT PIGUAL</button>
                        </div>
                    </div>
                </div>
            `;
        }

        function findPartnerMatches(name) {
            const n = name.toLowerCase().trim();
            return partners.filter(p =>
                p.nom.toLowerCase() === n ||
                (p.alias && p.alias.toLowerCase() === n) ||
                n.includes(p.nom.toLowerCase()) ||
                p.nom.toLowerCase().includes(n)
            );
        }

        function buildPartnerOptions(matches) {
            let options = '';
            if (matches.length === 0) {
                options += '<option>⚠️ Aucune correspondance</option>';
            } else if (matches.length === 1) {
                const p = matches[0];
                options += `<option selected>${p.nom}</option>`;
            } else {
                options += '<option>-- Sélectionner --</option>';
                matches.forEach(p => {
                    options += `<option>${p.nom}</option>`;
                });
            }
            options += '<option disabled>──── Tous les partenaires ────</option>';
            const matchIds = matches.map(p => p.id);
            partners.filter(p => !matchIds.includes(p.id)).forEach(p => {
                options += `<option>${p.nom}</option>`;
            });
            return options;
        }

        function filterPartners(transactionId, search) {
            const select = document.getElementById(`partner-${transactionId}`);
            const options = select.options;
            const searchLower = search.toLowerCase().trim();

            for (let i = 0; i < options.length; i++) {
                const text = options[i].text.toLowerCase();
                options[i].hidden = searchLower && !text.includes(searchLower) && !text.includes('────');
            }
        }

        function updateServices(transactionId) {
            const partnerSelect = document.getElementById(`partner-${transactionId}`);
            const serviceSelect = document.getElementById(`service-${transactionId}`);
            const selectedText = partnerSelect.value;

            if (!selectedText || selectedText.includes('⚠️') || selectedText.includes('────') || selectedText === '-- Sélectionner --') {
                serviceSelect.innerHTML = '<option selected>COLLECTE DE PAIEMENTS</option>';
                return;
            }

            const partnerName = selectedText.split(' (')[0].trim();
            const partner = partners.find(p => p.nom === partnerName);

            if (partner && partner.services && partner.services.length > 0) {
                serviceSelect.innerHTML = partner.services.map(s =>
                    `<option${s === 'COLLECTE DE PAIEMENTS' ? ' selected' : ''}>${s}</option>`
                ).join('');
            } else {
                serviceSelect.innerHTML = '<option selected>COLLECTE DE PAIEMENTS</option>';
            }
        }

        function showLoader() {
            document.getElementById('loader').classList.add('show');
        }

        function hideLoader() {
            document.getElementById('loader').classList.remove('show');
        }

        function showSuccess(title, message) {
            document.getElementById('successTitle').textContent = title;
            document.getElementById('successMessage').innerHTML = message;
            openModal('modalSuccess');
        }

        function handleValidation(id, type) {
            const config = {
                remboursement: {
                    btnId: 'btn-reversement',
                    stateKey: 'remboursement',
                    bridgeMethod: 'remboursement',
                    validatedText: '✓ REVERSEMENT VALIDÉ',
                    title: 'État de reversement',
                    message: 'État de reversement généré pour'
                },
                commission: {
                    btnId: 'btn-commission',
                    stateKey: 'commission',
                    bridgeMethod: 'commission',
                    validatedText: '✓ COMMISSION VALIDÉE',
                    title: 'État de commission',
                    message: 'État de commission généré pour'
                }
            }[type];

            const btn = document.getElementById(`${config.btnId}-${id}`);
            if (btn && btn.disabled) return;

            transactionStates[id][config.stateKey] = true;
            updateCardColor(id);
            updateFooter();
            updateActionsDropdown();
            if (bridge) bridge[config.bridgeMethod](id);

            if (btn) {
                btn.disabled = true;
                btn.textContent = config.validatedText;
            }

            const transaction = transactions.find(t => t.id === id);
            showSuccess(config.title, `${config.message} :<br><strong>${transaction.nom}</strong><br><br>Transaction: ${id}`);
        }

        function handleRemboursement(id) { handleValidation(id, 'remboursement'); }
        function handleCommission(id) { handleValidation(id, 'commission'); }

        function updateActionsDropdown() {
            const toggleActionBtn = (btnId, isDisabled, handler) => {
                const btn = document.getElementById(btnId);
                btn.classList.toggle('disabled', isDisabled);
                btn.onclick = isDisabled ? null : handler;
            };

            const pendingReversement = transactions.filter(t => !transactionStates[t.id].remboursement).length;
            toggleActionBtn('actionBulkReversement', pendingReversement === 0, handleBulkReversement);

            const transactionsWithCommission = transactions.filter(t => t.commission > 0);
            const pendingCommission = transactionsWithCommission.filter(t => !transactionStates[t.id].commission).length;
            toggleActionBtn('actionBulkCommission', !transactionsWithCommission.length || !pendingCommission, handleBulkCommission);
        }

        let currentTransactionId = null;

        function handleDTRF(id) {
            currentTransactionId = id;
            openModal('modalDTRF');
        }

        function handlePigual(id) {
            currentTransactionId = id;
            openModal('modalPigual');
        }

        function openModal(modalId) {
            document.getElementById(modalId).classList.add('active');
        }

        function closeModal(modalId) {
            document.getElementById(modalId).classList.remove('active');
            if (modalId === 'modalDTRF') {
                document.getElementById('formDTRF').reset();
            } else if (modalId === 'modalPigual') {
                document.getElementById('formPigual').reset();
            }
        }

        function submitDTRF(event) {
            event.preventDefault();
            const formData = new FormData(event.target);
            const data = Object.fromEntries(formData.entries());

            console.log('DTRF Data:', data, 'Transaction ID:', currentTransactionId);

            if (bridge) {
                bridge.dtrf(currentTransactionId);
            }

            closeModal('modalDTRF');
        }

        function submitPigual(event) {
            event.preventDefault();
            const formData = new FormData(event.target);
            const data = Object.fromEntries(formData.entries());

            console.log('Pigual Data:', data, 'Transaction ID:', currentTransactionId);

            if (bridge) {
                bridge.pigual(currentTransactionId);
            }

            closeModal('modalPigual');
        }

        // Fermer les modals en cliquant sur l'overlay
        document.addEventListener('click', function(e) {
            if (e.target.classList.contains('modal-overlay')) {
                closeModal(e.target.id);
            }
        });

        function updateCardColor(id) {
            const card = document.getElementById(`card-${id}`);
            const transaction = transactions.find(t => t.id === id);
            const state = transactionStates[id];

            card.className = 'transaction-card';

            if (transaction.agregation && state.remboursement) {
                card.classList.add('orange');
            } else if (transaction.commission && state.remboursement && state.commission) {
                card.classList.add('blue');
            } else if (!transaction.commission && !transaction.agregation && state.remboursement) {
                card.classList.add('green');
            }
        }

        function updateFooter() {
            const completed = transactions.filter(t => {
                const state = transactionStates[t.id];
                return t.commission ? (state.remboursement && state.commission) : state.remboursement;
            }).length;

            document.getElementById('completedCount').textContent = completed;
            document.getElementById('totalCount').textContent = transactions.length;
            document.getElementById('generateBtn').disabled = false;
        }

        function generatePDF() {
            showLoader();
            if (bridge) bridge.generatePDF();
        }

        function onPDFGenerated() {
            hideLoader();
            openModal('modalPDFGenerated');
        }

        function confirmReturnHome() {
            closeModal('modalPDFGenerated');
            if (bridge) {
                bridge.goBack();
            }
        }

        function formatCurrency(amount) {
            return new Intl.NumberFormat('fr-FR', { maximumFractionDigits: 0 }).format(amount) + ' F CFA';
        }

        function formatNumber(amount) {
            return new Intl.NumberFormat('fr-FR', { maximumFractionDigits: 0 }).format(amount);
        }

        function toggleDropdown() {
            document.getElementById('actionsDropdown').classList.toggle('active');
        }

        document.addEventListener('click', function(e) {
            const dropdown = document.getElementById('actionsDropdown');
            if (dropdown && !dropdown.contains(e.target)) {
                dropdown.classList.remove('active');
            }
        });

        function handleBulkReversement() {
            toggleDropdown();
            const pendingCount = transactions.filter(t => {
                const state = transactionStates[t.id];
                return !state.remboursement;
            }).length;

            if (pendingCount === 0) {
                showSuccess('Information', 'Tous les états de reversement sont déjà validés.');
                return;
            }

            document.getElementById('bulkReversementMessage').innerHTML =
                `Voulez-vous vraiment valider tous les états de reversement ?<br><br><strong>${pendingCount} transaction(s)</strong> seront affectées.`;
            openModal('modalBulkReversement');
        }

        function confirmBulkValidation(type) {
            const config = {
                remboursement: {
                    stateKey: 'remboursement',
                    btnId: 'btn-reversement',
                    bridgeMethod: 'remboursement',
                    validatedText: '✓ REVERSEMENT VALIDÉ',
                    modal: 'modalBulkReversement',
                    label: 'reversement'
                },
                commission: {
                    stateKey: 'commission',
                    btnId: 'btn-commission',
                    bridgeMethod: 'commission',
                    validatedText: '✓ COMMISSION VALIDÉE',
                    modal: 'modalBulkCommission',
                    label: 'commission',
                    filter: t => t.commission > 0
                }
            }[type];

            let count = 0;
            const transactionsToProcess = config.filter ? transactions.filter(config.filter) : transactions;

            transactionsToProcess.forEach(t => {
                if (!transactionStates[t.id][config.stateKey]) {
                    transactionStates[t.id][config.stateKey] = true;
                    updateCardColor(t.id);
                    if (bridge) bridge[config.bridgeMethod](t.id);

                    const btn = document.getElementById(`${config.btnId}-${t.id}`);
                    if (btn) {
                        btn.disabled = true;
                        btn.textContent = config.validatedText;
                    }
                    count++;
                }
            });

            updateFooter();
            updateActionsDropdown();
            closeModal(config.modal);
            showSuccess('Validation réussie', `<strong>${count} état(s) de ${config.label}</strong> ont été validés avec succès.`);
        }

        function confirmBulkReversement() { confirmBulkValidation('remboursement'); }
        function confirmBulkCommission() { confirmBulkValidation('commission'); }

        function handleBulkCommission() {
            toggleDropdown();
            const transactionsWithCommission = transactions.filter(t => t.commission > 0);
            const pendingCount = transactionsWithCommission.filter(t => !transactionStates[t.id].commission).length;

            if (!transactionsWithCommission.length) {
                showSuccess('Information', 'Aucune transaction n\'a de commission.');
                return;
            }

            if (!pendingCount) {
                showSuccess('Information', 'Tous les états de commission sont déjà validés.');
                return;
            }

            document.getElementById('bulkCommissionMessage').innerHTML =
                `Voulez-vous vraiment valider tous les états de commission ?<br><br><strong>${pendingCount} transaction(s)</strong> seront affectées.`;
            openModal('modalBulkCommission');
        }
    </script>
</body>