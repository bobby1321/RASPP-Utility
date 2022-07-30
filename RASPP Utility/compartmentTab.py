from math import floor

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QFrame, QPushButton, QRadioButton, QLineEdit, QComboBox, \
    QInputDialog, QMessageBox


class CompartmentTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.image = QLabel()
        pixmap = QPixmap("img\\thonk tonk.png")
        self.image.setPixmap(pixmap)
        self.layout.addWidget(self.image, 0, 0, alignment=Qt.AlignCenter)