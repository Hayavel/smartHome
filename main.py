from PySide6.QtWidgets import (QMainWindow, QApplication, QPushButton, QComboBox,
                               QProgressBar, QSlider, QLineEdit, QDial, QLabel,
                               QFrame, QRadioButton, QFileDialog)

from PySide6.QtGui import QPixmap, QIcon, QFontDatabase, QFont
from PySide6.QtCore import QSize, Qt

from element.warning import WarningDialog

import sys
import json
import time

#from smartDevice import Bulb
#from roundedImage import rounded_image
#import hexadecimal as hexDec
#import local_statistics as lStat


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('SmartDevice')
        self.setFixedSize(QSize(900, 750))
        self.setWindowIcon(QIcon('design/icon.ico'))
        font = QFont('Comfortaa', 24)
        font.setBold(True)
        self.setFont(font)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont('design/Comfortaa.ttf')
    window = MainWindow()
    window.show()
    app.exec()