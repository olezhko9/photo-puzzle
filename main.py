from PIL import Image
import os

def get_image_paths(folder):
    return (os.path.join(folder, f)
            for f in os.listdir(folder)
            if 'jpg' in f)


photo_name = 'frog.png'
img = Image.open(photo_name)
img.show()

folder = os.path.abspath('tiles/')
images = get_image_paths(folder)
print(list(images))