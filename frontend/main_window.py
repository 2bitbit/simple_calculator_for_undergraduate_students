from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QListWidget,
    QSplitter,
)
from . import widgets
from backend.server import Server
from PySide6.QtGui import QIcon, QFont
from utils import PATHS


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 50, 1200, 850)

        # 先启动服务器
        self.server = Server()
        self.server.start()

        # 设置主显示区域
        self.splitter = QSplitter(self)
        self.set_up_side_bar()
        self.set_up_content()
        self.splitter.setStretchFactor(0, 0)  # 设置左边侧边栏为不可拉伸
        self.splitter.setStretchFactor(1, 1)  # 设置右边内容区域为可拉伸
        self.setCentralWidget(self.splitter)

        # 美化主窗口
        self.setWindowTitle("Welcome to Sympy-GUI！")
        self.setWindowIcon(QIcon(PATHS["images_paths"]["icon"]))

    def set_up_side_bar(self):
        self.sidebar = QListWidget(self)
        self.sidebar.addItems(
            [
                "HomePage",
                "Calculus",
                "Linear Algebra",
                "Differential Equations",
                "Limit",
                "Plot",
            ]
        )
        self.sidebar.setFont(QFont("微软雅黑", 13, QFont.Bold))
        self.sidebar.currentItemChanged.connect(self.display_page)
        self.splitter.addWidget(self.sidebar)

        # 设置侧边栏宽度为200
        # 在添加到splitter后设置初始大小。注意：当你将widget添加到QSplitter后，QSplitter会接管这个widget的大小控制。所以不要在前面用self.sidebar.resize()
        sizes = self.splitter.sizes()
        sizes[0] = 200
        self.splitter.setSizes(sizes)

    def set_up_content(self):
        """创建右边的内容显示"""

        # 创建右边的部分
        self.content = QStackedWidget(self)
        self.splitter.addWidget(self.content)

        # 要显示的有哪些页面
        self.home_page = widgets.HomePage(self)
        self.content.addWidget(self.home_page)
        self.content.setCurrentWidget(self.home_page)
        
        self.calculus = widgets.CalculusFrontend(self)
        self.content.addWidget(self.calculus)
        
        self.linear_algebra = widgets.LinearAlgebraFrontend(self)
        self.content.addWidget(self.linear_algebra)
        
        self.differential_equations = widgets.DifferentialEquationsFrontend(self)
        self.content.addWidget(self.differential_equations)

        self.limit = widgets.Limit(self)
        self.content.addWidget(self.limit)

        self.plot = widgets.Plot(self)
        self.content.addWidget(self.plot)

    def display_page(self):
        item = self.sidebar.currentItem()
        text = item.text()
        if text == "HomePage":
            self.content.setCurrentWidget(self.home_page)
        elif text == "Calculus":
            self.content.setCurrentWidget(self.calculus)
        elif text == "Linear Algebra":
            self.content.setCurrentWidget(self.linear_algebra)
        elif text == "Differential Equations":
            self.content.setCurrentWidget(self.differential_equations)
        elif text == "Limit":
            self.content.setCurrentWidget(self.limit)
        elif text == "Plot":
            self.content.setCurrentWidget(self.plot)
