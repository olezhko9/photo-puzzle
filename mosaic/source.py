import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
import design
from PhotoPuzzle import PhotoPuzzle

# command_to_convert
# pyuic5 'D:\__main__\Python\photo puzzle\design.ui' -o 'D:\__main__\Python\photo puzzle\design.py'


class PuzzleWorker(QThread):
    def __init__(self, source_img_path, tiles_path, *args):
        super().__init__()
        self.args = args
        self.puzzle = PhotoPuzzle(source_img_path, tiles_path)

    def run(self):
        self.puzzle.create_photo_puzzle(*self.args)


class PhotoPuzzleApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pictureButton.clicked.connect(self.open_photo)
        self.directoryButton.clicked.connect(self.choose_directory)
        self.runButton.clicked.connect(self.run)
        self.progressLayout.hide()

    def open_photo(self):
        self.photo_path = QFileDialog.getOpenFileName(self, 'Выберите файл', 'c:\\', "Image files (*.jpg *.png)")[0]
        qpix = QPixmap(self.photo_path)
        photo_name = os.path.split(self.photo_path)[1]
        self.pictureLabel.setText(photo_name)
        self.pixmapLabel.setPixmap(qpix.scaledToWidth(self.pixmapLabel.width()))

    def choose_directory(self):
        self.directory = QFileDialog.getExistingDirectory(self, "Выберите папку")
        files_in_directory = len(os.listdir(self.directory))
        self.directoryLabel.setText("Плиток: {0}".format(files_in_directory))

    def show_progress(self):
        progress = self.puzzleWorker.puzzle.progress
        if progress == 100:
            self.timer.stop()
        self.progressBar.setValue(progress)

    def run(self):
        self.progressLayout.show()
        photo_path = os.path.abspath(self.photo_path)
        folder = os.path.abspath(self.directory)
        # photo_path = os.path.abspath('frog.png')
        # folder = os.path.abspath('tiles/')
        pix_tile = int(self.pixelsTileLEdit.text())
        process_num = int(self.processLEdit.text())
        # pix_tile = 4
        # process_num = -1

        self.puzzleWorker = PuzzleWorker(photo_path, folder, pix_tile, process_num)
        self.puzzleWorker.start()

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.show_progress)
        self.timer.start()


""" Debug function"""
def qt_message_handler(mode, context, message):
    if mode == QtInfoMsg:
        mode = 'INFO'
    elif mode == QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    print('qt_message_handler: line: %d, func: %s(), file: %s' % (
        context.line, context.function, context.file))
    print('  %s: %s\n' % (mode, message))

qInstallMessageHandler(qt_message_handler)


def main():
    app = QApplication(sys.argv)
    window = PhotoPuzzleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
