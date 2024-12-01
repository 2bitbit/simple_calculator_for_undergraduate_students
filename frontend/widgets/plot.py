from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
import sympy
from sympy.plotting import plot, plot3d
from sympy import plot_implicit
from sympy import Eq
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 解决中文字体显示异常问题
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示异常问题


class Plot(QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        self.variable_list = []
        self.main_layout_QVBoxLayout = QVBoxLayout(self)
        self.setup_ui()

    def setup_ui(self):
        # 设置变量与区间
        self.setting_variable_layout_QHBoxLayout = QHBoxLayout()
        self.main_layout_QVBoxLayout.addLayout(self.setting_variable_layout_QHBoxLayout)

        tmp_layout_QVBoxLayout = QVBoxLayout()
        self.setting_variable_layout_QHBoxLayout.addLayout(tmp_layout_QVBoxLayout)
        self.variable_name_1_QlineEdit = QLineEdit(self)
        self.variable_name_1_QlineEdit.setPlaceholderText("输入x轴变量名（默认为x）")
        self.variable_name_1_QlineEdit.setFixedWidth(250)
        tmp_layout_QVBoxLayout.addWidget(self.variable_name_1_QlineEdit)
        self.variable_interval_1_QlineEdit = QLineEdit(self)
        self.variable_interval_1_QlineEdit.setPlaceholderText(
            "输入x轴区间（数字与,的组合）"
        )
        self.variable_interval_1_QlineEdit.setFixedWidth(300)
        tmp_layout_QVBoxLayout.addWidget(self.variable_interval_1_QlineEdit)

        tmp_layout_QVBoxLayout = QVBoxLayout()
        self.setting_variable_layout_QHBoxLayout.addLayout(tmp_layout_QVBoxLayout)
        self.variable_name_2_QlineEdit = QLineEdit(self)
        self.variable_name_2_QlineEdit.setPlaceholderText("输入y轴变量名（默认为y）")
        self.variable_name_2_QlineEdit.setFixedWidth(250)
        tmp_layout_QVBoxLayout.addWidget(self.variable_name_2_QlineEdit)

        # 设置区间
        tmp_layout_QHBoxLayout = QHBoxLayout()
        self.main_layout_QVBoxLayout.addLayout(tmp_layout_QHBoxLayout)
        for i in self.variable_list:
            tmp_QLabel = QLabel(i, self)
            tmp_layout_QHBoxLayout.addWidget(tmp_QLabel)

        # 普通函数
        tmp_layout_QHBoxLayout = QHBoxLayout()
        self.main_layout_QVBoxLayout.addLayout(tmp_layout_QHBoxLayout)

        tmp_QLabel = QLabel("普通函数：输入只含x轴变量的表达式", self)
        tmp_QLabel.setFixedHeight(30)
        tmp_QLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        tmp_layout_QHBoxLayout.addWidget(tmp_QLabel)

        self.input_QLineEdit_1 = QLineEdit(self)
        tmp_layout_QHBoxLayout.addWidget(self.input_QLineEdit_1)

        self.button_QPushButton_1 = QPushButton("绘制", self)
        self.button_QPushButton_1.clicked.connect(self.plot_normal)
        tmp_layout_QHBoxLayout.addWidget(self.button_QPushButton_1)

        # 隐函数
        tmp_layout_QHBoxLayout = QHBoxLayout()
        self.main_layout_QVBoxLayout.addLayout(tmp_layout_QHBoxLayout)

        tmp_QLabel = QLabel("隐函数", self)
        tmp_QLabel.setFixedHeight(30)
        tmp_QLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        tmp_layout_QHBoxLayout.addWidget(tmp_QLabel)

        self.input_QLineEdit_2_1 = QLineEdit(self)
        self.input_QLineEdit_2_1.setPlaceholderText("输入隐函数左部分")
        tmp_layout_QHBoxLayout.addWidget(self.input_QLineEdit_2_1)

        tmp_QLabel = QLabel("=", self, font=QFont("Consolas", 20))
        tmp_layout_QHBoxLayout.addWidget(tmp_QLabel)

        self.input_QLineEdit_2_2 = QLineEdit(self)
        self.input_QLineEdit_2_2.setPlaceholderText("输入隐函数右部分")
        tmp_layout_QHBoxLayout.addWidget(self.input_QLineEdit_2_2)

        self.button_QPushButton_2 = QPushButton("绘制", self)
        self.button_QPushButton_2.clicked.connect(self.plot_implicit)
        tmp_layout_QHBoxLayout.addWidget(self.button_QPushButton_2)

        # 三维图
        # y轴区间
        self.variable_interval_2_QlineEdit = QLineEdit(self)
        self.variable_interval_2_QlineEdit.setPlaceholderText(
            "输入y轴区间（数字与,的组合）"
        )
        self.variable_interval_2_QlineEdit.setFixedWidth(300)
        self.main_layout_QVBoxLayout.addWidget(self.variable_interval_2_QlineEdit)

        # z轴名字
        self.variable_name_3_QlineEdit = QLineEdit(self)
        self.variable_name_3_QlineEdit.setPlaceholderText(
            "输入z轴变量名（可选）（默认为z）"
        )
        self.main_layout_QVBoxLayout.addWidget(self.variable_name_3_QlineEdit)

        # 三维图表达式
        tmp_layout_QHBoxLayout = QHBoxLayout()
        self.main_layout_QVBoxLayout.addLayout(tmp_layout_QHBoxLayout)
        tmp_QLabel = QLabel("三维图：输入只含x轴和y轴变量的表达式", self)
        tmp_QLabel.setFixedHeight(30)
        tmp_QLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        tmp_layout_QHBoxLayout.addWidget(tmp_QLabel)

        self.input_QLineEdit_3 = QLineEdit(self)
        tmp_layout_QHBoxLayout.addWidget(self.input_QLineEdit_3)

        self.button_QPushButton_3 = QPushButton("绘制", self)
        self.button_QPushButton_3.clicked.connect(self.plot_3d)
        tmp_layout_QHBoxLayout.addWidget(self.button_QPushButton_3)

    def plot_normal(self):
        self.update_variable_list()
        x = getattr(self, self.variable_list[0])
        y = getattr(self, self.variable_list[1])
        intervals = self.variable_interval_1_QlineEdit.text().split(",")
        if not all(intervals):
            intervals = [-10, 10]
        left_endpoint = int(intervals[0])
        right_endpoint = int(intervals[1])
        plot(
            sympy.sympify(self.input_QLineEdit_1.text()),
            (x, left_endpoint, right_endpoint),
            aspect_ratio=[1, 1],
            ylabel=str(y),
        )

    def plot_implicit(self):
        self.update_variable_list()
        x = getattr(self, self.variable_list[0])
        y = getattr(self, self.variable_list[1])
        left_part = sympy.sympify(self.input_QLineEdit_2_1.text())
        right_part = sympy.sympify(self.input_QLineEdit_2_2.text())
        plot_implicit(
            Eq(left_part, right_part),
            aspect_ratio=[1, 1],
            x_var=x,
            y_var=y,
        )

    def plot_3d(self):
        self.update_variable_list()
        x = getattr(self, self.variable_list[0])
        y = getattr(self, self.variable_list[1])
        z = getattr(self, self.variable_list[2])
        intervals = {
            x: (
                list(map(int, self.variable_interval_1_QlineEdit.text().split(",")))
                if all(self.variable_interval_1_QlineEdit.text().split(","))
                else [-10, 10]
            ),
            y: (
                list(map(int, self.variable_interval_2_QlineEdit.text().split(",")))
                if all(self.variable_interval_2_QlineEdit.text().split(","))
                else [-10, 10]
            ),
        }
        plot3d(
            sympy.sympify(self.input_QLineEdit_3.text()),
            (x, intervals[x][0], intervals[x][1]),
            (y, intervals[y][0], intervals[y][1]),
            x_var=x,
            y_var=y,
            zlabel=str(z),
        )

    def update_variable_list(self):
        default_variable_list = ["x", "y", "z"]
        lst = [
            self.variable_name_1_QlineEdit.text(),
            self.variable_name_2_QlineEdit.text(),
            self.variable_name_3_QlineEdit.text(),
        ]
        for i in range(len(lst)):
            if not lst[i]:
                lst[i] = default_variable_list[i]
        self.variable_list = lst
        for name in self.variable_list:
            setattr(self, name, sympy.symbols(name))
