# Meme Generator – Instructions

## Overview

Use Python and Flask to generate memes randomly or with user input. This project aims to build a "meme generator" – a multimedia application to dynamically create memes, including an image with an overlaid quote. Users can make memes by providing image URLs and quotes, author text.

### Quote Engine Module

Parses the file mentioned above and creates a quote model for those, a structured way of clearly showing a quote with the context (body) and the author.

### Meme Generator Module

 Put the quote on the image to create the meme.

### Installation

`pip install -r requirements.txt`

### Built using

    Flask: Simple web server interface
    CSV: Easy processing meme text from csv files
    Pillow: Image processing to add text
    pdftotext: command-line utility for converting PDF files to plain text files

### CLI Functions

```
$ python3 meme.py -h
usage: meme.py [-h] [--path PATH] [--body BODY] [--author AUTHOR]

Show me a meme

optional arguments:
  -h, --help       show this help message and exit
  --path PATH      path to an image
  --body BODY      quote body to add to the image
  --author AUTHOR  quote author to add to the image

```

### Web App Start up 

once start navigate to /127.0.0.1:5000/

```
$ python3 app.py 
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```