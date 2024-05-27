"""
The IngestorInterface module provides an abstract base class for ingestors.

It defines the IngestorInterface class which sets,
the structure for all ingestor classes,
ensuring they implement the can_ingest and parse methods.
"""

# Import the necessary modules from the typing library
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


# Define the IngestorInterface class, which is an abstract base class
class IngestorInterface(ABC):
    """Abstract base class for all ingestors."""

    # Define the can_ingest method as an abstract class method
    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Determine if the given file can be ingested.

        :param path: Path to the file to be ingested
        :return: True if the file can be ingested, False otherwise
        """
        pass

    # Define the parse method as an abstract class method
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the given file to extract quotes.

        :param path: Path to the file to be ingested
        :return: List of QuoteModel instances
        """
        pass
