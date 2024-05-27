"""
The CSVIngestor class for ingesting quotes from CSV files.

The CSVIngestor class reads CSV files and extracts quotes from them.
"""

# Import the necessary modules
import pandas as pd
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


# Define the CSVIngestor class that inherits from IngestorInterface
class CSVIngestor(IngestorInterface):
    """Concrete ingestor class for CSV files."""

    # Define the class variable for supported file types
    allowed_extensions = ['csv']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Given file can be ingested based on its extension.

        :param path: Path to the file to be ingested
        :return: True if the file extension is
        in the allowed extensions, False otherwise
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the given CSV file to extract quotes.

        :param path: Path to the CSV file to be ingested
        :return: List of QuoteModel instances
        """
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file " +
                             "with extension {path.split('.')[-1]}")

        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(path)

        # Initialize an empty list to hold QuoteModel instances
        quotes = []

        # Iterate through each row in the DataFrame
        # and create a QuoteModel instance
        for _, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
