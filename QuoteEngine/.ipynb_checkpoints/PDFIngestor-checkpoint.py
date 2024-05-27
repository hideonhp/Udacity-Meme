"""
The PDFIngestor class for ingesting quotes from PDF files.

The PDFIngestor class uses the pdftotext tool to
convert PDFs to text and then extracts quotes.
"""

# Import the necessary modules
import subprocess
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


# Define the PDFIngestor class that inherits from IngestorInterface
class PDFIngestor(IngestorInterface):
    """Concrete ingestor class for PDF files."""

    # Define the class variable for supported file types
    allowed_extensions = ['pdf']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Determine if the given file can be ingested based on its extension.

        :param path: Path to the file to be ingested
        :return: True if the file extension is in the allowed extensions,
                 False otherwise
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the given PDF file to extract quotes.

        :param path: Path to the PDF file to be ingested
        :return: List of QuoteModel instances
        """
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file with" +
                             " extension {path.split('.')[-1]}")

        # Use subprocess to execute
        # the pdftotext command to convert the PDF to text
        process = subprocess.Popen(
            ['pdftotext', path, '-'],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        # Decode the output from bytes to string and split it into lines
        pdf_text = stdout.decode('utf-8').split('\n')

        # Initialize an empty list to hold QuoteModel instances
        quotes = []

        # Iterate through each line in the converted text
        for line in pdf_text:
            if line.strip():  # Check if the line is not empty
                # Split the line into body
                # and author using the '-' delimiter
                parse = line.split('-')
                if len(parse) == 2:
                    body, author = parse
                    new_quote = QuoteModel(body.strip(), author.strip())
                    quotes.append(new_quote)

        return quotes
