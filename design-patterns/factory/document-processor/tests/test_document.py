import unittest

from document import *


class TestDocumentProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = PresentationDocumentProcessor("presentation")

    def test_inheritance(self):
        self.assertIsInstance(
            self.processor,
            DocumentProcessor,
            "If there is a common parent DocumentProcessor class, the PresentationDocumentProcessor class should inherit from it",
        )

    def test_fields(self):
        self.assertTrue(
            hasattr(self.processor, "document_name"),
            "If there is a common parent DocumentProcessor class, it should have a document_name field",
        )

    def test_methods(self):
        self.assertTrue(
            hasattr(self.processor, "supports_type"),
            "If there is a common parent DocumentProcessor class, it should have a supports_type method",
        )
        self.assertTrue(
            hasattr(self.processor, "process_document"),
            "If there is a common parent DocumentProcessor class, it should have a process_document method",
        )

    def test_type_check(self):
        self.assertIsInstance(
            self.processor.document_name,
            str,
            "If there is a common parent DocumentProcessor class, the document_name field should be a string",
        )


class TestAudioPlayerFactory(unittest.TestCase):
    def test_create_presentation(self):
        presentation = DocumentFactory.create_document(
            DocumentType.PRESENTATION, "presentation"
        )
        self.assertIsInstance(
            presentation,
            PresentationDocumentProcessor,
            "If the requested format is Presentation, the factory should return a PresentationDocumentProcessor",
        )

    def test_create_spreadsheet(self):
        spreadsheet = DocumentFactory.create_document(
            DocumentType.SPREADSHEET, "spreadsheet"
        )
        self.assertIsInstance(
            spreadsheet,
            SpreadsheetDocumentProcessor,
            "If the requested format is Spreadsheet, the factory should return a SpreadsheetDocumentProcessor",
        )

    def test_create_text(self):
        text = DocumentFactory.create_document(DocumentType.TEXT, "text")
        self.assertIsInstance(
            text,
            TextDocumentProcessor,
            "If the requested format is Text, the factory should return a TextDocumentProcessor",
        )


if __name__ == "__main__":
    unittest.main()
