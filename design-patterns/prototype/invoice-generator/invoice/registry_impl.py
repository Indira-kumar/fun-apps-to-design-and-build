from __future__ import annotations

from typing import Optional, Dict

from .invoice_model import Invoice, InvoiceType
from .registry import InvoicePrototypeRegistry

class InvoicePrototypeRegistryImpl(InvoicePrototypeRegistry):

    def __init__(self):
        self.prototypes: Dict[InvoiceType, Invoice] = {}

    def add_prototype(self, invoice: Invoice) -> None:
        self.prototypes[invoice.type_] = invoice

    def get_prototype(self, type_: InvoiceType) -> Optional[Invoice]:
        if type_ not in self.prototypes:
            return None
        return self.prototypes[type_]

    def clone(self, type_: InvoiceType) -> Optional[Invoice]:
        if type_ not in self.prototypes:
            return None
        return self.prototypes[type_].clone_object()