"""
The TextIngestor module provides functionality to parse quotes from TXT files.

It defines the TextIngestor class that extends the IngestorInterface to handle
TXT files specifically.
"""

# Import the necessary modules
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


# Define the TextIngestor class that inherits from IngestorInterface
class TextIngestor(IngestorInterface):
    """Concrete ingestor class for TXT files."""

    # Define the class variable for supported file types
    allowed_extensions = ['txt']

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
        Parse the given TXT file to extract quotes.

        :param path: Path to the TXT file to be ingested
        :return: List of QuoteModel instances
        """
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file with" +
                             " extension {path.split('.')[-1]}")

        # Initialize an empty list to hold QuoteModel instances
        quotes = []

        # Open and read the text file line by line
        with open(path, 'r', encoding='utf-8-sig') as file:
            for line in file:
                if line.strip():  # Check if the line is not empty
                    # Split the line into body
                    # and author using the '-' delimiter
                    parse = line.split('-')
                    if len(parse) == 2:
                        body, author = parse
                        new_quote = QuoteModel(body.strip(), author.strip())
                        quotes.append(new_quote)

        return quotes
