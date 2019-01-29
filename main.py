from PIL import Image
import os
import time
from multiprocessing import Pool


class PhotoPuzzle:

    def __init__(self, source_img_path, tiles_path):
        self.image = Image.open(source_img_path)
        self.tiles_path = tiles_path
        self.pix_to_tile = 4
        self.tile_size = 32

    def load_tiles(self):
        return (os.path.join(self.tiles_path, f) for f in os.listdir(self.tiles_path) if 'jpg' in f)

    def show_source_img(self):
        self.image.show()

    def get_img_mid_color(self, img, x_start=0, y_start=0, x_crop=None, y_crop=None):
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

        total_pix = x_crop * y_crop
        rgb = (red // total_pix, green // total_pix, blue // total_pix)

        return rgb

    def distance_between_colors(self, color_1, color_2):
        return sum(map(lambda x, y: (y-x)**2, color_1, color_2))

    def find_best_tile(self, pix):
        min_distance = 3 * 256 ** 2
        x = pix[0]
        y = pix[1]
        crop_mid_color = self.get_img_mid_color(self.image, x, y, self.pix_to_tile, self.pix_to_tile)
        tile_filename = None

        for color in self.tiles_mid_colors:
            distance = self.distance_between_colors(color[1], crop_mid_color)
            if distance < min_distance:
                min_distance = distance
                tile_filename = color[0]

        return tile_filename

    def create_photo_puzzle(self, pix_to_tile=4, njobs=1):
        if njobs == -1:
            njobs = os.cpu_count()

        self.pix_to_tile = pix_to_tile
        photo_puzzle = Image.new(mode="RGB", size=(self.image.width // self.pix_to_tile * self.tile_size,
                                                   self.image.height // self.pix_to_tile * self.tile_size))
        self.tiles_mid_colors = []
        for t in list(puzzle.load_tiles()):
            self.tiles_mid_colors.append((t, puzzle.get_img_mid_color(Image.open(t), 0, 0, self.tile_size, self.tile_size)))

        tiles_pos = []
        for x in range(0, self.image.width, self.pix_to_tile):
            for y in range(0, self.image.height, self.pix_to_tile):
                tiles_pos.append([x, y])

        with Pool(njobs) as pool:
            tile_filename = pool.map(self.find_best_tile, tiles_pos)
            pool.close()
            pool.join()

        for idx, pos in enumerate(tiles_pos):
            tile_img = Image.open(tile_filename[idx])
            x = pos[0]
            y = pos[1]
            photo_puzzle.paste(im=tile_img, box=(x // self.pix_to_tile * self.tile_size,
                                                 y // self.pix_to_tile * self.tile_size,
                                                 x // self.pix_to_tile * self.tile_size + self.tile_size,
                                                 y // self.pix_to_tile * self.tile_size + self.tile_size))
            print(str(round(idx / len(tiles_pos) * 100)) + "% completed")
        base, puzzle_name = os.path.split(self.image.filename)
        path_to_save = os.path.join(base, 'puzzle-{0}-{1}'.format(self.pix_to_tile, puzzle_name))
        photo_puzzle.save(path_to_save)
        return path_to_save


if __name__ == "__main__":
    photo_path = os.path.abspath('frog.png')
    folder = os.path.abspath('tiles/')

    start = time.time()
    puzzle = PhotoPuzzle(photo_path, folder)
    puzzle.create_photo_puzzle(pix_to_tile=2, njobs=-1)
    print(time.time() - start)
