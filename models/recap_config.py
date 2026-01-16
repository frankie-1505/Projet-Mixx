from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional


class ConditionReglement(Enum):
    JOURNALIER = "JOURNALIER"
    HEBDOMADAIRE = "HEBDOMADAIRE"
    MENSUEL = "MENSUEL"
    PERSONNALISER = "PERSONNALISER"


@dataclass
class RecapConfig:
    titre: str
    condition_reglement: ConditionReglement
    mode_paiement: str
    excel_path: str
    periode_debut: Optional[date] = None
    periode_fin: Optional[date] = None
