"""
This module provides the DocxIngestor class for parsing DOCX files.

The DocxIngestor class extracts quotes from DOCX files and converts them
into QuoteModel instances.
"""

# Import the necessary modules
from typing import List
from docx import Document
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


# Define the DocxIngestor class that inherits from IngestorInterface
class DocxIngestor(IngestorInterface):
    """Concrete ingestor class for DOCX files."""

    # Define the class variable for supported file types
    allowed_extensions = ['docx']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Determine if the given file can be ingested based on its extension.

        :param path: Path to the file to be ingested
        :return: True if the file extension is in the allowed extensions
        False otherwise
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the given DOCX file to extract quotes.

        :param path: Path to the DOCX file to be ingested
        :return: List of QuoteModel instances
        """
        if not cls.can_ingest(path):
            raise ValueError(
                f"Cannot ingest file with extension {path.split('.')[-1]}"
            )

        # Load the DOCX file using the Document class from the docx module
        document = Document(path)

        # Initialize an empty list to hold QuoteModel instances
        quotes = []

        # Iterate through each paragraph in the document
        for para in document.paragraphs:
            if para.text.strip():  # Check if the paragraph text is not empty
                # Split the paragraph text into body
                # and author using the '-' delimiter
                parse = para.text.split('-')
                if len(parse) == 2:
                    body, author = parse
                    new_quote = QuoteModel(body.strip(), author.strip())
                    quotes.append(new_quote)

        return quotes
