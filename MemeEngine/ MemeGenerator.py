from PIL import Image, ImageDraw, ImageFont

import textwrap

class MemeGenerator():
    """Class to generate a meme."""
    def __init__(self, image_location, text, author, width):
        """Create a new meme for self"""
        self.image_location = image_location
        self.text = text
        self.author = author
        self.width = width

    def make_meme(image_location, text, author, width=500):
        """Create a new meme.
        :param image_location: path of the image
        :param text: quote for the meme
        :param author: author of the quote
        :param width: width of the meme image - default set to 500
        :return: path of the meme
        """

        image = Image.open(image_location)
        names = text.split(' ')
        static_path = 'static/' + names[-1] + '_meme.jpg'

        if width is not None:
            ratio = float(width)/float(image.size[0])
            height = int(ratio * float(image.size[1]))
            image = image.resize((width, height), Image.NEAREST)
        message = text + " -" + author
        wrapper = textwrap.TextWrapper(width=50)
        message = wrapper.fill(text=message)

        if message is not None:
            draw = ImageDraw.Draw(image)
            draw.text((10, 30), message)
            image.save(static_path)
        return static_path