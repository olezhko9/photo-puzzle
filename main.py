from PIL import Image
import os


class PhotoPuzzle:

    def __init__(self, source_img_path, tiles_path, pix_to_tile=4):
        self.image = Image.open(source_img_path)
        self.source_img_path = source_img_path
        self.tiles_path = tiles_path
        self.pix_to_tile = pix_to_tile

    def load_tiles(self):
        return (os.path.join(self.tiles_path, f) for f in os.listdir(self.tiles_path) if 'jpg' in f)

    def show_source_img(self):
        self.image.show()

    def get_img_mid_color(self, img, x_start=0, y_start=0, x_crop=None, y_crop=None):
        img = Image.open(img)
        if x_crop is None:
            x_crop = img.width
        if y_crop is None:
            y_crop = img.height

        pix = img.crop([x_start, y_start, x_start + x_crop, y_start + y_crop]).load()
        red, green, blue = 0, 0, 0

        for x in range(x_crop):
            for y in range(y_crop):
                red += pix[x, y][0]
                green += pix[x, y][1]
                blue += pix[x, y][2]

        img.close()
        total_pix = x_crop * y_crop
        rgb = (red // total_pix, green // total_pix, blue // total_pix)

        return rgb


if __name__ == "__main__":
    photo_path = os.path.abspath('frog.png')
    folder = os.path.abspath('tiles/')

    puzzle = PhotoPuzzle(photo_path, folder, 8)
    puzzle.show_source_img()
    print(puzzle.get_img_mid_color(photo_path))

    tile_size = (0, 0, 32, 32)
    for t in list(puzzle.load_tiles()):
        print(t, puzzle.get_img_mid_color(t, *tile_size))