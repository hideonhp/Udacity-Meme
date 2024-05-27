"""
Flask application for generating and displaying memes.

The application allows users to view
random memes and create custom memes by
providing an image URL and a quote.
It uses the QuoteEngine to parse quotes and
the MemeEngine to create meme images.
"""


# Import the necessary modules and functions
import random
import os
import logging
import requests
import textwrap
from flask import Flask, render_template, request
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize the Flask application
app = Flask(__name__)

# Set up directories
meme = MemeEngine('./static')


# Define a route for the main page
@app.route('/')
def meme_rand():
    """
    Generate a random meme.

    :return: Rendered HTML template for the random meme page
    """
    img_dir = './_data/photos/dog/'
    quote_dir = './_data/DogQuotes'

    img = random.choice(os.listdir(img_dir))
    img_path = os.path.join(img_dir, img)

#     for file in os.listdir('./_data/DogQuotes'):
#         file_path = f'./_data/DogQuotes/{file}'
#         if Ingestor.can_ingest(file_path):
#             quotes.extend(Ingestor.parse(file_path))
    quotes = Ingestor.parse_directory(quote_dir)
    quote = random.choice(quotes)

    # Wrap the text if it's too long
    wrapped_text = textwrap.fill(quote.body, width=40)

    path = meme.make_meme(img_path, quote.body, quote.author)
    return render_template('meme.html', path=path)


# Define a route for creating a meme with user input
@app.route('/create', methods=['GET'])
def meme_form():
    """
    Display a form for user to input data for a custom meme.

    :return: Rendered HTML template for the meme creation form
    """
    return render_template('meme_form.html')


# Define a route for processing the form data and generating the meme
@app.route('/create', methods=['POST'])
def meme_post():
    """
    Create a meme with user-provided data.

    :return: Rendered HTML template for the created meme
    """
    image_url = request.form['image_url']
    quote_body = request.form['body']
    quote_author = request.form['author']

    try:
        response = requests.get(image_url, timeout=5)
        # Check if the request was successful
        response.raise_for_status()

        # response = requests.get(image_url)
        img = f'./static/{random.randint(0, 1000000)}.jpg'
        with open(img, 'wb') as f:
            f.write(response.content)

        path = meme.make_meme(img, quote_body, quote_author)
        os.remove(img)
        return render_template('meme.html', path=path)

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching image from URL: {e}")
        return render_template(
            'meme_error.html',
            message="Invalid image URL, please try again.")

    except Exception as e:
        logging.error(f"Error generating meme: {e}")
        return render_template(
            'meme_error.html',
            message="An error occurred while" +
            " generating the meme. Please try again.")

#     except Exception as e:
#         print(f"Error: {e}")
#         return render_template('meme_error.html')


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True, port=5000)
