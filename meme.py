"""
This module provides functionality to generate memes with optional quotes.

It uses the QuoteEngine to parse quotes
from various file types and the MemeEngine
to create meme images with those quotes.
"""


# Import the necessary modules and functions
import os
import random
import argparse
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """
    Generate a meme given an image path, quote body, and quote author.

    :param path: Path to the input image
    :param body: Quote body text
    :param author: Quote author
    :return: Path to the generated meme image
    """
    img = None
    quote = None

    if path is None:
        # Select a random image if no path is provided
        images = "./_data/photos/dog/"
        imgs = [os.path.join(images, img) for img in os.listdir(images)]
        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        # Select a random quote if no body is provided
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for file in quote_files:
            quotes.extend(Ingestor.parse(file))
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author is required if body is provided')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Generate a meme with an optional quote."
    )
    parser.add_argument('--path', type=str, help="Path to the image file")
    parser.add_argument('--body', type=str, help="Quote body text")
    parser.add_argument('--author', type=str, help="Quote author")

    args = parser.parse_args()

    print(generate_meme(args.path, args.body, args.author))
