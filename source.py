import sys
import os
from PyQt5 import QtWidgets, Qt
import design
from PhotoPuzzle import PhotoPuzzle
# command_to_convert
# pyuic5 'D:\__main__\Python\photo puzzle\design.ui' -o 'D:\__main__\Python\photo puzzle\design.py'
class PhotoPuzzleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.file_Button.clicked.connect(self.open_photo)
        self.folder_Button.clicked.connect(self.choose_directory)
        self.ren_Button.clicked.connect(self.run)

    def open_photo(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл', 'c:\\', "Image files (*.jpg *.png)")
        self.photo_path = fname[0]
        self.file_Label.setText(self.photo_path)
        self.label.setPixmap(Qt.QPixmap(self.photo_path))

    def choose_directory(self):
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")

    def run(self):
        photo_path = os.path.abspath(self.photo_path)
        folder = os.path.abspath(self.directory)
        puzzle = PhotoPuzzle(photo_path, folder)
        puzzle.create_photo_puzzle(pix_to_tile=2, njobs=-1)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = PhotoPuzzleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()