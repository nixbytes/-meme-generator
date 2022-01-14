import random
import os
import requests
from flask import Flask, render_template, abort, request
import PIL
import QuoteEngine
from QuoteEngine.Ingestor import Ingestor
from MemeEngine.MemeGenerator import MemeGenerator
from QuoteEngine import QuoteModel

app = Flask(__name__)

def setup():
    """ Load all resources """

    quote_files = ["./_data/DogQuotes/DogQuotesTXT.txt",
                   "./_data/DogQuotes/DogQuotesDOCX.docx",
                   "./_data/DogQuotes/DogQuotesPDF.pdf",
                   "./_data/DogQuotes/DogQuotesCSV.csv"
                   ]

    quotes = []
    for file in quote_files:
        try:
            quotes.extend(Ingestor.parse(file))
        except TypeError:
            print(f'{file} extension unsupported')
            continue

    images_path = "./_data/photos/dog/"

    imgs = [
        os.path.join(images_path, image)
        for image in os.listdir(images_path)
        if image.endswith('.jpg')
    ]

    return quotes, imgs

quotes, imgs = setup()

@app.route('/')
def meme_rand():
    """ Generate a random meme """  
    img =  random.choice(imgs)
    quote = random.choice(quotes)
    path = MemeGenerator.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    url = request.form['image_url']
    quote = QuoteEngine.QuoteModel(request.form["body"], request.form["author"])
    img = requests.get(url)
    temp_path = f"./tmp/{random.randint(0, 100000)}.png"
    open(temp_path, 'wb').write(img.content)
    path = MemeGenerator.make_meme(temp_path, quote.body, quote.author)
    return render_template('meme.html', path=path)         

if __name__ == "__main__":
    app.run()
