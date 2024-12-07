import sys
import os

if getattr(sys, "frozen", False):
    BASE_PATH = sys._MEIPASS
else:
    BASE_PATH = os.path.dirname(os.path.dirname(__file__))

FONTS_PATHS = {
    "方正基础像素": os.path.join(BASE_PATH, "resources/fonts/方正基础像素.ttf"),
    "Pandora_Rogtars": os.path.join(BASE_PATH, "resources/fonts/Pandora_Rogtars.otf"),
}

IMAGES_PATHS = {
    "background": os.path.join(BASE_PATH, "resources/images/background.png"),
    "icon": os.path.join(BASE_PATH, "resources/images/icon.ico"),
    "tray_icon": os.path.join(BASE_PATH, "resources/images/tray_icon.ico"),
}

PATHS = {
    "fonts_paths": FONTS_PATHS,
    "images_paths": IMAGES_PATHS,
    "mathjax_path": "http://localhost:8000/"
    + "resources/mathjax/MathJax-4.0.0-beta.7/tex-mml-chtml.js",
}
