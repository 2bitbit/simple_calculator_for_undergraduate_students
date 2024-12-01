from frontend import MainWindow
from PySide6.QtWidgets import QApplication
import utils

if __name__ == "__main__":
    app = QApplication(["sympy-gui"])
    utils.load_fonts()
    window = MainWindow()
    window.show()
    app.exec()
