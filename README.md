# Meme Generator

## Description
The Meme Generator is a simple Python application that generates memes by adding quotes to images. It takes an image file, a quote, and the author of the quote as input and produces a meme with the quote overlaid on the image... Or you can simply using by press "Random" button

## Features
- Generate memes by adding quotes to images
- Supports various image formats
- Automatically resizes images to maintain aspect ratio
- Customizable output directory for generated memes
- Error handling for invalid input and file operations

## Set Up a Virtual Environment
```
sudo apt-get update
sudo apt-get install poppler-utils
pip install virtualenv
virtualenv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Validate code style and docs style
```
clear && printf '\e[3J'
pycodestyle . --exclude=.venv
pydocstyle .
```

## Project Structure
```
project_directory/
|-- QuoteEngine/
| |-- init.py
| |-- IngestorInterface.py
| |-- CSVIngestor.py
| |-- DocxIngestor.py
| |-- PDFIngestor.py
| |-- TextIngestor.py
| |-- Ingestor.py
| |-- QuoteModel.py
|-- MemeEngine/
| |-- init.py
| |-- MemeEngine.py
|-- _data/
| |-- SimpleLines/
| |-- DogQuotes/
|-- app.py
|-- templates/
|-- README.md
```

## Usage
1. Run the Flask application by setting the Flask app and running the server:
    ```
    export FLASK_APP=app.py
    flask run --host 0.0.0.0 --port 3000 --reload
    ```
2. Access the application in your web browser by navigating to `http://localhost:3000`. Or click on "Open Preview" on Udacity workspace

## Dependencies
- Python 3.6.3
- Pillow
- Flask
- pandas
- python-docx
- xpdf (for PDF parsing)

## Module
MemeEngine

```
The MemeEngine module handles the creation of memes by overlaying quotes onto images. It includes functionality for loading images, resizing them, adding text, and saving the final image.
```
QuoteEngine

```
The QuoteEngine module is responsible for loading and parsing quotes from various file formats. It consists of several sub-modules:

- QuoteModel: Encapsulates the body and author of a quote.
- IngestorInterface: Abstract base class that defines the interface for all ingestors.
- CSVIngestor: Parses quotes from CSV files.
- DocxIngestor: Parses quotes from DOCX files.
- PDFIngestor: Parses quotes from PDF files using xpdf.
- TextIngestor: Parses quotes from TXT files.
- Ingestor: Aggregates all the individual ingestors and selects the appropriate one based on file type.
```