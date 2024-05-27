"""
The QuoteModel module defines the QuoteModel class.

This class encapsulates a quote with a body and an author.
"""


# Define the QuoteModel class
class QuoteModel:
    """Encapsulate a quote with a body and an author."""

    def __init__(self, body: str, author: str):
        """
        Initialize a QuoteModel instance.

        :param body: The body of the quote
        :param author: The author of the quote
        """
        self.body = body
        self.author = author

    def __str__(self) -> str:
        """
        Return a string representation of the QuoteModel instance.

        :return: Formatted string with the quote body and author
        """
        return f'"{self.body}" - {self.author}'

    def __repr__(self) -> str:
        """
        Return representation of the QuoteModel instance for debugging.

        :return: Formal string representation
        with the class name and attributes
        """
        return f'QuoteModel(body="{self.body}", author="{self.author}")'
