from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

class MemeGenerator:
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
        static_path = 'content/' + names[-1].strip() + '.jpeg'

        if width is not None:
            ratio = float(width)/float(image.size[0])
            height = int(ratio * float(image.size[1]))
            image = image.resize((width, height), Image.NEAREST)

        wrapper = textwrap.TextWrapper(width=50)
        text_message = f"{text}"
        text_message = wrapper.fill(text=text_message)

        author_message = f"{author}"
        author_message = wrapper.fill(text=author_message)

        font = ImageFont.truetype('fonts/Roboto-Regular.ttf', 50)

        if text_message or author_message is not None:
            draw = ImageDraw.Draw(image)

            draw.text((10, 30), text_message, font=font, fill='white')
            draw.text((300, 400), author_message, font=font, fill='white')
            if not os.path.isdir('./content/'):
                os.makedirs('./content/')
            image.save(static_path)

        return static_path