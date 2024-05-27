"""
Responsible for extracting quotes from various file formats.

This package provides the following modules and classes:
- QuoteModel: A class to encapsulate a quote body and its author.
- IngestorInterface: An abstract base class defining the interface.
- CSVIngestor: A class to parse quotes from CSV files.
- DocxIngestor: A class to parse quotes from DOCX files.
- PDFIngestor: A class to parse quotes from PDF files.
- TextIngestor: A class to parse quotes from TXT files.
- Ingestor: A class to select the appropriate ingestor based on the file type.
"""

# Import the QuoteModel class from the QuoteModel module
from .QuoteModel import QuoteModel

# Import the IngestorInterface class from the IngestorInterface module
from .IngestorInterface import IngestorInterface

# Import the CSVIngestor class from the CSVIngestor module
from .CSVIngestor import CSVIngestor

# Import the DocxIngestor class from the DocxIngestor module
from .DocxIngestor import DocxIngestor

# Import the PDFIngestor class from the PDFIngestor module
from .PDFIngestor import PDFIngestor

# Import the TextIngestor class from the TextIngestor module
from .TextIngestor import TextIngestor

# Import the Ingestor class from the Ingestor module
from .Ingestor import Ingestor
