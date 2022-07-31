from math import floor
import os, sys
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
        pixmap = QPixmap(self.resourcePath("img/thonktonk.png"))
        self.image.setPixmap(pixmap)
        self.layout.addWidget(self.image, 0, 0, alignment=Qt.AlignCenter)

    def resourcePath(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)