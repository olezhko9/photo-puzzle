import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
import design
from PhotoPuzzle import PhotoPuzzle

# command_to_convert
# pyuic5 'D:\__main__\Python\photo puzzle\design.ui' -o 'D:\__main__\Python\photo puzzle\design.py'

class PhotoPuzzleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pictureButton.clicked.connect(self.open_photo)
        self.directoryButton.clicked.connect(self.choose_directory)
        self.runButton.clicked.connect(self.run)

    def open_photo(self):
        self.photo_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл', 'c:\\', "Image files (*.jpg *.png)")[0]
        qpix = QPixmap(self.photo_path)
        photo_name = os.path.split(self.photo_path)[1]
        self.pictureLabel.setText(photo_name)
        self.pixmapLabel.setPixmap(qpix.scaledToWidth(self.pixmapLabel.width()))


    def choose_directory(self):
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        files_in_directory = len(os.listdir(self.directory))
        self.directoryLabel.setText("Плиток: {0}".format(files_in_directory))

    def run(self):
        photo_path = os.path.abspath(self.photo_path)
        folder = os.path.abspath(self.directory)
        puzzle = PhotoPuzzle(photo_path, folder)
        pix_tile = int(self.pixelsTileLEdit.text())
        process_num = int(self.processLEdit.text())
        puzzle.create_photo_puzzle(pix_to_tile=pix_tile, njobs=process_num)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = PhotoPuzzleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()