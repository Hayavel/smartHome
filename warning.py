from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel

class WarningDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Error!")

        QBtn = QDialogButtonBox.StandardButton.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Check Type, Name, ID, IP, KEY or Version of your device!")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class RemoveDeviceDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Remove Device")

        QBtn = QDialogButtonBox.StandardButton.Yes | QDialogButtonBox.StandardButton.No

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel('Are you sure you want to remove this device?')
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)