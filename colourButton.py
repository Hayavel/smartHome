from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

class ColourButton(QPushButton):
    def __init__(self):
        super().__init__()

        image = QIcon('design/plus.png')
        self.setIcon(image)
        self.setIconSize(QSize(28, 28))