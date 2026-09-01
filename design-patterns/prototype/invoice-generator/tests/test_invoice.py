import unittest

from invoice import Invoice, InvoiceType, InvoicePrototypeRegistryImpl


class TestInvoicePrototypeRegistryImpl(unittest.TestCase):

    def setUp(self):
        self.registry = InvoicePrototypeRegistryImpl()

        # Sample invoices
        self.standard_invoice = Invoice(
            1, "John Doe", 100.0, "Credit Card", InvoiceType.STANDARD
        )
        self.proforma_invoice = Invoice(
            2, "Jane Smith", 200.0, "PayPal", InvoiceType.PRO_FORMA
        )

        # Add sample invoices to the registry
        self.registry.prototypes = {
            InvoiceType.STANDARD: self.standard_invoice,
        }

    def test_clone_object(self):
        # Test cloning the invoice object
        cloned_invoice = self.standard_invoice.clone_object()
        self.assertIsNot(
            cloned_invoice,
            self.standard_invoice,
            "If an object is cloned, it should not be the same as the original.",
        )
        self.assertEqual(
            cloned_invoice.invoice_id,
            self.standard_invoice.invoice_id,
            "If an object is cloned, the invoice ID should be the same as the original.",
        )
        self.assertEqual(
            cloned_invoice.type_,
            self.standard_invoice.type_,
            "If an object is cloned, the type_ should be the same as the original.",
        )

    def test_clone(self):
        # Test cloning an existing invoice
        cloned_invoice = self.registry.clone(InvoiceType.STANDARD)

        self.assertIsNotNone(
            cloned_invoice, "If the invoice exists, it should be cloned."
        )
        self.assertEqual(
            cloned_invoice.invoice_id,
            self.standard_invoice.invoice_id,
            "If the invoice exists, the invoice ID should be the same as the original.",
        )
        self.assertEqual(
            cloned_invoice.customer_name,
            self.standard_invoice.customer_name,
            "If the invoice exists, the customer name should be the same as the original.",
        )
        self.assertEqual(
            cloned_invoice.amount,
            self.standard_invoice.amount,
            "If the invoice exists, the amount should be the same as the original.",
        )
        # Add more assertions for other fields

        # Test cloning a non-existent invoice
        non_existent_clone = self.registry.clone(InvoiceType.RECURRING)
        self.assertIsNone(
            non_existent_clone, "If the invoice does not exist, it should return None."
        )

    def test_add_prototype(self):
        # Test adding a new prototype
        initial_size = len(self.registry.prototypes)
        self.registry.add_prototype(self.proforma_invoice)

        self.assertEqual(
            len(self.registry.prototypes),
            initial_size + 1,
            "If a new prototype is added, the size of the registry should increase by 1.",
        )

        proforma_invoice = self.registry.prototypes[InvoiceType.PRO_FORMA]
        self.assertEqual(
            proforma_invoice,
            self.proforma_invoice,
            "If a new prototype is added, it should be accessible from the registry.",
        )

    def test_get_prototype(self):
        # Test getting an existing prototype
        standard_invoice = self.registry.get_prototype(InvoiceType.STANDARD)
        self.assertEqual(
            standard_invoice,
            self.standard_invoice,
            "If the invoice exists, it should be accessible from the registry.",
        )

        # Test getting a non-existent prototype
        non_existent_invoice = self.registry.get_prototype(InvoiceType.RECURRING)
        self.assertIsNone(
            non_existent_invoice,
            "If the invoice does not exist, it should return None.",
        )


if __name__ == "__main__":
    unittest.main()
