"""
This module contains the MemeEngine class which is used to generate memes.

The MemeEngine class adds quotes to images and saves the resulting
memes to the specified directory.
"""

from PIL import Image, ImageDraw, ImageFont
import os
import random
import textwrap


class MemeEngine:
    """A class to generate memes by adding quotes to images."""

    def __init__(self, output_dir: str):
        """
        Initialize the MemeEngine instance.

        :param output_dir: The directory where generated memes will be saved
        """
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(
        self,
        img_path: str,
        text: str,
        author: str,
        width=500
    ) -> str:
        """
        Create a meme with a quote on an image.

        :param img_path: Path to the input image
        :param text: The quote body
        :param author: The quote author
        :param width: The desired width of the meme (default is 500px)
        :return: Path to the generated meme image
        """
        try:
            # Open the image
            img = Image.open(img_path)

#             # Calculate the height to maintain aspect ratio
#             original_width, original_height = img.size
#             aspect_ratio = width / float(img.size[0])
#             height = int(aspect_ratio * float(img.size[1]))
#             img = img.resize((width, height), Image.NEAREST)

            # Resize the image
            original_width, original_height = img.size
            aspect_ratio = original_height / original_width
            new_height = int(aspect_ratio * width)
            img = img.resize((width, new_height), Image.ANTIALIAS)

            # Prepare to draw on the image
            wrapped_text = textwrap.fill(text, width=40)
            wrapped_author = textwrap.fill(author, width=40)
            quote = f'{wrapped_text} - {wrapped_author}'
            font = ImageFont.load_default()

            # Prepare the text to be drawn
            draw = ImageDraw.Draw(img)

            # Calculate text position
            text_width, text_height = draw.textsize(quote, font=font)
            x = random.randint(0, width - text_width)
            y = random.randint(0, new_height - text_height)

            # Draw the text on the image
            draw.text((x, y), quote, font=font, fill='white')

            # Generate the output path
            output_path = os.path.join(
                self.output_dir,
                f'meme_{random.randint(0, 1000000)}.jpg')

            # Save the image
            img.save(output_path)

            return output_path

        except Exception as e:
            print(f"Error generating meme with error: {e}")
            return None
