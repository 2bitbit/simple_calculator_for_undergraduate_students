from .paths import PATHS
from PySide6.QtGui import QFontDatabase


def load_fonts():
    for font_path in PATHS["fonts_paths"].values():
        QFontDatabase.addApplicationFont(font_path)
