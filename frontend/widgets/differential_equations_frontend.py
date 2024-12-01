from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt   

class DifferentialEquationsFrontend(QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        self.main_layout_QVBoxLayout = QVBoxLayout(self)
        self.main_layout_QVBoxLayout.setAlignment(Qt.AlignTop)
        
        
        self.label = QLabel("Differential Equations\nTo be continued", self)
        self.main_layout_QVBoxLayout.addWidget(self.label)
