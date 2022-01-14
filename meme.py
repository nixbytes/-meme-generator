import os
import random
import argparse

from QuoteEngine.Ingestor import Ingestor
from MemeEngine.MemeGenerator import MemeGenerator
from QuoteEngine import QuoteModel


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote"""
    quotes = []
    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]
        img = random.choice(imgs)
    else:
        img = path
    if body is None:
        quote_files = [
            "./_data/DogQuotes/DogQuotesTXT.txt",
            "./_data/DogQuotes/DogQuotesDOCX.docx",
            "./_data/DogQuotes/DogQuotesCSV.csv",
        ]
        for file in quote_files:
            quotes.extend(Ingestor.parse(file))
        quote = random.choice(quotes)
        path = MemeGenerator.make_meme(img, quote.body, quote.author)
    elif author is None:
        raise Exception("Author Required if Body is Used")
    else:
        path = MemeGenerator.make_meme(img, body, author)
    return path


if __name__ == "__main__":
    """
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    """

    parser = argparse.ArgumentParser(description="Show me a meme")
    parser.add_argument("--path", type=str, default=None, help="path to an image")
    parser.add_argument(
        "--body", type=str, default=None, help="quote body to add to the image"
    )
    parser.add_argument(
        "--author", type=str, default=None, help="quote author to add to the image"
    )
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
