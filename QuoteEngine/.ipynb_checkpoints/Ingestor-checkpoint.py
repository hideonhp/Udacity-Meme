"""
This module provides the Ingestor class for parsing different file types.

The Ingestor class determines the appropriate helper class to use
for a given file type to extract quotes.
"""

# Import the necessary modules
import os
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


# Define the Ingestor class that inherits from IngestorInterface
class Ingestor(IngestorInterface):
    """
    The Ingestor class.

    Encapsulates the logic to select the appropriate
    helper for a given file type.
    """

    # Define the list of ingestors
    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Determine if any of the ingestor classes can ingest the given file.

        :param path: Path to the file to be ingested
        :return: True if any ingestor class can ingest the file
        False otherwise
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return True
        return False

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the given file to extract quotes using the appropriate ingestor.

        :param path: Path to the file to be ingested
        :return: List of QuoteModel instances
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise ValueError(
            f"No suitable ingestor found for file" +
            " with extension {path.split('.')[-1]}"
        )

    @classmethod
    def parse_directory(cls, directory: str) -> List[QuoteModel]:
        """
        Parse all ingestible files in the given directory to extract quotes.

        :param directory: Path to the directory containing files to be ingested
        :return: List of QuoteModel instances
        """
        quotes = []
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if cls.can_ingest(file_path):
                    quotes.extend(cls.parse(file_path))
        return quotes
