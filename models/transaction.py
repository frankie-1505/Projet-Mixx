from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Optional


class TransactionType(Enum):
    SIMPLE = "simple"
    COMMISSION = "commission"
    AGREGATION = "agregation"


class TransactionState(Enum):
    PENDING = "pending"
    REMBOURSEMENT_DONE = "remboursement_done"
    COMPLETED = "completed"


@dataclass
class Transaction:
    id: str
    nom: str
    date_debut: date
    date_fin: date
    montant_trans: float
    montant_reverse: float
    alias: str = ""
    agregation: str = ""
    annulation: str = ""
    commission: float = 0.0
    partner_id: Optional[str] = None
    service: str = "-"
    champ1: str = ""
    champ2: str = ""
    state: TransactionState = field(default=TransactionState.PENDING)

    @property
    def transaction_type(self) -> TransactionType:
        if self.agregation:
            return TransactionType.AGREGATION
        if self.commission > 0:
            return TransactionType.COMMISSION
        return TransactionType.SIMPLE

    @property
    def is_completed(self) -> bool:
        if self.transaction_type == TransactionType.COMMISSION:
            return self.state == TransactionState.COMPLETED
        return self.state in (TransactionState.REMBOURSEMENT_DONE, TransactionState.COMPLETED)

    def mark_remboursement_done(self):
        if self.transaction_type == TransactionType.COMMISSION:
            self.state = TransactionState.REMBOURSEMENT_DONE
        else:
            self.state = TransactionState.COMPLETED

    def mark_commission_done(self):
        if self.transaction_type == TransactionType.COMMISSION:
            self.state = TransactionState.COMPLETED
