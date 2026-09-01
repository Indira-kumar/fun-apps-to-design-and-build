from dataclasses import dataclass
from enum import Enum
from abc import ABC, abstractmethod


@dataclass
class DocumentProcessor(ABC):
    document_name: str

    def __init__(self, document_name: str):
        self.document_name = document_name

    @abstractmethod
    def supports_type(self):
        pass

    @abstractmethod
    def process_document(self):
        pass

@dataclass
class PresentationDocumentProcessor(DocumentProcessor):
    document_name: str

    def supports_type(self):
        return DocumentType.PRESENTATION

    def process_document(self):
        print(f"Processing a presentation document: {self.document_name}")

    def add_slide(self):
        print("Adding a slide to the presentation.")


@dataclass
class SpreadsheetDocumentProcessor(DocumentProcessor):
    document_name: str

    def supports_type(self):
        return DocumentType.SPREADSHEET

    def process_document(self):
        print(f"Processing a spreadsheet document: {self.document_name}")

    def perform_data_analysis(self):
        print("Performing data analysis on the spreadsheet.")


@dataclass
class TextDocumentProcessor(DocumentProcessor):
    document_name: str

    def supports_type(self):
        return DocumentType.TEXT

    def process_document(self):
        print(f"Processing a text document: {self.document_name}")


class DocumentType(Enum):
    PRESENTATION = "Presentation"
    SPREADSHEET = "Spreadsheet"
    TEXT = "Text"
