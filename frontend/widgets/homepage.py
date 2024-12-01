from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class HomePage(QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        self.layout = QVBoxLayout(self)

        # 标题
        self.label_1 = QLabel("HomePage", self)
        self.label_1.setFont(QFont("Pandora Rogtars", 50))
        self.label_1.setFixedSize(500, 100)
        self.label_1.setAlignment(Qt.AlignTop)
        self.layout.addWidget(self.label_1)

        # 欢迎的主要内容
        self.label_2 = QLabel("欢迎来到Sympy-GUI！", self)
        self.label_2.setFont(QFont("FZJCXS", 150))
        self.label_2.setAlignment(Qt.AlignTop)
        self.layout.addWidget(self.label_2)
