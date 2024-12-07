from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QMessageBox,
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from PySide6.QtWebEngineWidgets import QWebEngineView
import sympy
from sympy.printing import latex
from utils import PATHS
from ..html_template import html_template
from backend import output_process
from backend import CalculusBackend


class CalculusFrontend(QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        self.backend = CalculusBackend()
        self.main_layout_QVBoxLayout = QVBoxLayout(self)
        self.setup_ui()

    def setup_ui(self):
        """建立界面"""

        # 输入框
        self.input_QLineEdit = QLineEdit(self)
        self.input_QLineEdit.setPlaceholderText(
            "输入数学表达式(键入回车是直接计算结果或化简式子)"
        )
        self.input_QLineEdit.returnPressed.connect(self.compute)
        self.main_layout_QVBoxLayout.addWidget(self.input_QLineEdit)

        # 功能们：
        # 变量相关：
        # 输入格式提示：
        tmp_QLabel = QLabel("变量格式：输入变量，以逗号隔开", self)
        tmp_QLabel.setFixedHeight(30)
        tmp_QLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.main_layout_QVBoxLayout.addWidget(tmp_QLabel)

        # 变量相关控件的横向布局
        variable_QHBoxLayout = QHBoxLayout()
        self.main_layout_QVBoxLayout.addLayout(variable_QHBoxLayout)

        # 添加变量
        tmp_layout = QVBoxLayout()
        tmp_layout.setSpacing(5)  # 输入框与按钮之间的间距
        self.add_variable_QLineEdit = QLineEdit(self)
        self.add_variable_QLineEdit.returnPressed.connect(self.add_variable)
        self.add_variable_QPushButton = QPushButton("添加变量", self)
        self.add_variable_QPushButton.setFixedWidth(100)
        self.add_variable_QPushButton.clicked.connect(self.add_variable)

        tmp_layout.addWidget(self.add_variable_QLineEdit)
        tmp_layout.addWidget(
            self.add_variable_QPushButton, 0, Qt.AlignmentFlag.AlignHCenter
        )  # 此处不可以用AlignCenter，否则按钮会在整个大方块居中，而不是在原来的长条里水平居中
        variable_QHBoxLayout.addLayout(tmp_layout)

        # 删除变量
        tmp_layout = QVBoxLayout()
        tmp_layout.setSpacing(5)
        self.delete_variable_QLineEdit = QLineEdit(self)
        self.delete_variable_QLineEdit.returnPressed.connect(self.remove_variable)
        self.delete_variable_QPushButton = QPushButton("删除变量", self)
        self.delete_variable_QPushButton.setFixedWidth(100)
        self.delete_variable_QPushButton.clicked.connect(self.remove_variable)

        tmp_layout.addWidget(self.delete_variable_QLineEdit)
        tmp_layout.addWidget(
            self.delete_variable_QPushButton, 0, Qt.AlignmentFlag.AlignHCenter
        )
        variable_QHBoxLayout.addLayout(tmp_layout)

        # 覆盖已有的变量的设置
        tmp_layout = QVBoxLayout()
        tmp_layout.setSpacing(5)
        self.overwrite_variable_QLineEdit = QLineEdit(self)
        self.overwrite_variable_QLineEdit.returnPressed.connect(self.overwrite_variable)
        self.overwrite_variable_QPushButton = QPushButton("覆盖变量", self)
        self.overwrite_variable_QPushButton.setFixedWidth(100)
        self.overwrite_variable_QPushButton.clicked.connect(self.overwrite_variable)

        tmp_layout.addWidget(self.overwrite_variable_QLineEdit)
        tmp_layout.addWidget(
            self.overwrite_variable_QPushButton, 0, Qt.AlignmentFlag.AlignHCenter
        )
        variable_QHBoxLayout.addLayout(tmp_layout)

        # 设置整体布局的间距
        variable_QHBoxLayout.setSpacing(10)  # 设置水平布局的间距
        self.main_layout_QVBoxLayout.setSpacing(10)  # 设置垂直布局的间距

        # 求导
        tmp_layout = QHBoxLayout()
        self.diff_QLabel = QLabel("输入格式：输入求导的变量,求导的阶数", self)
        self.diff_QLabel.setFixedWidth(300)
        self.diff_QLineEdit = QLineEdit(self)
        self.diff_QPushButton = QPushButton("求导", self)
        self.diff_QPushButton.clicked.connect(self.differentiate)
        self.diff_QPushButton.setFixedWidth(100)

        tmp_layout.addWidget(self.diff_QLabel)
        tmp_layout.addWidget(self.diff_QLineEdit)
        tmp_layout.addWidget(self.diff_QPushButton)
        self.main_layout_QVBoxLayout.addLayout(tmp_layout)

        # 求不定积分
        tmp_layout = QHBoxLayout()
        self.undefinite_integrate_QLabel = QLabel(
            "输入格式：输入要求不定积分的变量", self
        )
        self.undefinite_integrate_QLabel.setFixedWidth(300)
        self.undefinite_integrate_QLineEdit = QLineEdit(self)
        self.undefinite_integrate_QPushButton = QPushButton("求不定积分", self)
        self.undefinite_integrate_QPushButton.clicked.connect(self.undefinite_integrate)
        self.undefinite_integrate_QPushButton.setFixedWidth(100)

        tmp_layout.addWidget(self.undefinite_integrate_QLabel)
        tmp_layout.addWidget(self.undefinite_integrate_QLineEdit)
        tmp_layout.addWidget(self.undefinite_integrate_QPushButton)
        self.main_layout_QVBoxLayout.addLayout(tmp_layout)

        # 求定积分
        tmp_layout = QHBoxLayout()
        self.definite_integrate_QLabel = QLabel(
            "输入格式：输入要求定积分的变量,积分下限,积分上限", self
        )
        self.definite_integrate_QLabel.setFixedWidth(350)
        self.definite_integrate_QLineEdit = QLineEdit(self)
        self.definite_integrate_QPushButton = QPushButton("求定积分", self)
        self.definite_integrate_QPushButton.clicked.connect(self.definite_integrate)
        self.definite_integrate_QPushButton.setFixedWidth(100)

        tmp_layout.addWidget(self.definite_integrate_QLabel)
        tmp_layout.addWidget(self.definite_integrate_QLineEdit)
        tmp_layout.addWidget(self.definite_integrate_QPushButton)
        self.main_layout_QVBoxLayout.addLayout(tmp_layout)

        # 在某一点的泰勒展开式子
        tmp_layout = QHBoxLayout()
        self.taylor_QLabel = QLabel(
            "输入格式：输入要求泰勒展开的变量,展开点,展开阶数", self
        )
        self.taylor_QLabel.setFixedWidth(350)
        self.taylor_QLineEdit = QLineEdit(self)
        self.taylor_QPushButton = QPushButton("泰勒展开", self)
        self.taylor_QPushButton.clicked.connect(self.taylor)
        self.taylor_QPushButton.setFixedWidth(100)

        tmp_layout.addWidget(self.taylor_QLabel)
        tmp_layout.addWidget(self.taylor_QLineEdit)
        tmp_layout.addWidget(self.taylor_QPushButton)
        self.main_layout_QVBoxLayout.addLayout(tmp_layout)

        # 显示已有的变量
        self.variable_QLabel = QLabel(self, font=QFont("微软雅黑", 13, QFont.Bold))
        self.variable_QLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.variable_QLabel.setFixedHeight(30)
        self.update_variable_names_list()
        self.main_layout_QVBoxLayout.addWidget(self.variable_QLabel)

        # 结果显示
        self.result_QWebEngineView = QWebEngineView(self)
        self.result_QWebEngineView.setHtml(
            html_template.format(content="$$ \\text{准备就绪} $$")
        )  # 作用：预加载 MathJax
        self.main_layout_QVBoxLayout.addWidget(self.result_QWebEngineView)

    def update_variable_names_list(self):
        """更新变量名字列表"""
        if not self.backend.variables:
            self.variable_QLabel.setText("当前没有任何变量")
            return
        else:
            str = "当前变量有："
            for name in self.backend.variables[:-1]:
                str += name + ", "
            str += self.backend.variables[-1]
            self.variable_QLabel.setText(str)

    def add_variable(self):
        """添加变量"""
        try:
            # 获取并清理输入
            to_add_var_names = [
                name.strip()
                for name in self.add_variable_QLineEdit.text().split(",")
                if name.strip()
            ]

            # 验证变量名是否合法
            if not all(name.isidentifier() for name in to_add_var_names):
                raise ValueError("存在非法变量名")

            # 验证变量是否已存在
            for i in to_add_var_names:
                if i in self.backend.variables:
                    raise ValueError(f"变量{i}已存在")

            self.backend.add_variable(to_add_var_names)
            self.update_variable_names_list()

        except Exception as e:
            QMessageBox.warning(self, "错误", f"错误：{str(e)}")

    def remove_variable(self):
        """删除变量"""
        try:
            # 当前没有变量：
            if not self.backend.variables:
                raise ValueError("当前没有变量")

            # 当前有变量：
            to_remove_var_names = [
                name.strip()
                for name in self.delete_variable_QLineEdit.text().split(",")
                if name.strip()
            ]
            # 验证变量是否存在
            for name in to_remove_var_names:
                if name not in self.backend.variables:
                    raise ValueError(f"变量{name}不存在")
            else:  # 确定所有变量都是已有变量后再删除变量
                self.backend.remove_variable(to_remove_var_names)
                self.update_variable_names_list()
        except Exception as e:
            QMessageBox.warning(self, "错误", f"错误：{str(e)}")

    def overwrite_variable(self):
        """覆盖已有的变量的设置"""
        var_names = [
            name.strip()
            for name in self.overwrite_variable_QLineEdit.text().split(",")
            if name.strip()
        ]
        self.backend.overwrite_variable(var_names)
        self.update_variable_names_list()

    def update_result(self, content: str):
        """更新显示结果的统一接口，直接把 content 原文输出到 QWebEngineView"""
        html_content = html_template.format(content=f"$$ {content} $$")
        self.result_QWebEngineView.setHtml(html_content)

    def compute(self):
        """计算结果并显示结果"""
        expr = self.get_expression_sympy()
        self.update_result(output_process(expr))

    def differentiate(self):
        """计算导数并显示结果"""
        if not self.backend.variables:
            return
        expr = self.get_expression_sympy()
        if expr is None:
            return
        input = self.diff_QLineEdit.text().split(",")
        result = self.backend.differentiate(expr, input[0], int(input[1]))
        self.update_result(output_process(result))

    def undefinite_integrate(self):
        """计算不定积分并显示结果"""
        if not self.backend.variables:
            return
        expr = self.get_expression_sympy()
        if expr is None:
            return
        input = self.undefinite_integrate_QLineEdit.text().split(",")
        result = self.backend.undefinite_integrate(expr, input[0])
        self.update_result(output_process(result))

    def definite_integrate(self):
        """计算定积分并显示结果"""
        if not self.backend.variables:
            return
        expr = self.get_expression_sympy()
        if expr is None:
            return
        input = self.definite_integrate_QLineEdit.text().split(",")
        result = self.backend.definite_integrate(expr, input[0], input[1], input[2])
        self.update_result(output_process(result))

    def taylor(self):
        """计算在某一点的泰勒展开式子并显示结果"""
        if not self.backend.variables:
            return
        expr = self.get_expression_sympy()
        if expr is None:
            return
        input = self.taylor_QLineEdit.text().split(",")
        result = self.backend.taylor(expr, input[0], int(input[1]), int(input[2]))
        self.update_result(output_process(result))

    def get_expression_sympy(self) -> sympy.Expr:
        """获取并解析输入的数学表达式"""
        expression = self.input_QLineEdit.text()
        try:
            expr = sympy.sympify(expression)
            expr = sympy.simplify(expr)
            return expr
        except:
            QMessageBox.warning(self, "错误", "输入的表达式不合法")
            return None
