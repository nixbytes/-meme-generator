# Meme Generator – Instructions

Use Python and Flask to generate memes randomly or with user input. The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote. 

Overview

A multimedia application to dynamically generate memes, including an image with an overlaid quote. User can make meme by providing image url and quote, author text.

Installation

pip install -r requirements.txt

Built With

    Flask: Simple web server interface
    CSV: Easy processing meme text from csv files
    Pillow: Image processing to add text
    pdftotext: command-line utility for converting PDF files to plain text files

CLI Functions

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

Web App Start up

```
$ python3 app.py 
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```