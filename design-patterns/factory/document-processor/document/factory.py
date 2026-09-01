from .products import DocumentType, TextDocumentProcessor, SpreadsheetDocumentProcessor, \
    DocumentProcessor, PresentationDocumentProcessor

class DocumentFactory:
    _registry = {
        DocumentType.PRESENTATION: PresentationDocumentProcessor,
        DocumentType.TEXT: TextDocumentProcessor,
        DocumentType.SPREADSHEET: SpreadsheetDocumentProcessor
    }

    @classmethod
    def create_document(cls, type_: DocumentType, document_name: str) -> DocumentProcessor:
        try:
            document_processor_class = cls._registry[type_]
        except KeyError:
            raise ValueError('Unsupported document type: ', type_)

        return document_processor_class(document_name)