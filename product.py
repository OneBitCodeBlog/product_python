from PIL import Image
import re
import os

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    
    def add_thumbnail(self, image_path, size):
        image = Image.open(os.getcwd() + "/" + image_path)
        name = re.search('(?<=\/)\w+', image_path).group(0)
        image.thumbnail(size)
        thumb_name = name + str(size[0]) + "x" + str(size[1]) + "." + image.format
        image.save(os.getcwd() + "/thumbnails/" + thumb_name)

