from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton
from PySide6.QtWebEngineWidgets import QWebEngineView
import sympy
from backend.core.common_backend import output_process
from ..html_template import html_template


class Limit(QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        self.main_layout_QVBoxLayout = QVBoxLayout(self)
        self.setup_ui()

    def setup_ui(self):
        """建立界面"""

        # 输入框
        self.input_QLineEdit_1 = QLineEdit(self)
        self.input_QLineEdit_1.setPlaceholderText("输入表达式")
        self.main_layout_QVBoxLayout.addWidget(self.input_QLineEdit_1)

        self.input_QLineEdit_2 = QLineEdit(self)
        self.input_QLineEdit_2.setPlaceholderText("输入变量")
        self.main_layout_QVBoxLayout.addWidget(self.input_QLineEdit_2)

        self.input_QLineEdit_3 = QLineEdit(self)
        self.input_QLineEdit_3.setPlaceholderText("输入趋近的点")
        self.main_layout_QVBoxLayout.addWidget(self.input_QLineEdit_3)

        # 按钮
        self.button_QPushButton = QPushButton("计算", self)
        self.button_QPushButton.clicked.connect(self.compute)
        self.main_layout_QVBoxLayout.addWidget(self.button_QPushButton)

        # 输出框
        self.result_QWebEngineView = QWebEngineView(self)
        self.result_QWebEngineView.setHtml(
            html_template.format(content="$$ \\text{准备就绪} $$")
        )  # 作用：预加载 MathJax
        self.main_layout_QVBoxLayout.addWidget(self.result_QWebEngineView)

    def compute(self):
        """计算极限"""

        self.expression = sympy.sympify(self.input_QLineEdit_1.text())
        self.set_variable()
        self.point = sympy.sympify(self.input_QLineEdit_3.text())

        result = sympy.limit(self.expression, self.variable, self.point)
        self.update_result(output_process(result))

    def set_variable(self):
        """设置变量"""
        variable = self.input_QLineEdit_2.text().strip()
        if not variable.isidentifier():
            raise ValueError("变量名不合法")
        else:
            self.variable = sympy.symbols(variable)

    def update_result(self, content: str):
        """更新显示结果的统一接口，直接把content原文输出到QWebEngineView"""
        html_content = html_template.format(content=f"$$ {content} $$")
        self.result_QWebEngineView.setHtml(html_content)
