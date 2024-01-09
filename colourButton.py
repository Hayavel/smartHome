from PySide6.QtWidgets import QPushButton

class ColourButton(QPushButton):
    def __init__(self):
        super().__init__()

        self.setStyleSheet('image: url(design/plus.png);')