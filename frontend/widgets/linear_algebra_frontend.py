from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTabWidget,
    QTableWidget, QTableWidgetItem, QLineEdit, QMessageBox, QLabel, QDialog, QFormLayout, QDialogButtonBox, QSpinBox
)
from PySide6.QtCore import Qt
from PySide6.QtWebEngineWidgets import QWebEngineView
from backend.core.linear_algebra_backend import LinearAlgebraBackend
import sympy
from frontend.html_template import html_template
'''此部分主要由o1-mini编写。感恩。'''

class LinearAlgebraFrontend(QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        self.backend = LinearAlgebraBackend()
        self.main_layout_QVBoxLayout = QVBoxLayout(self)
        self.setup_ui()

    def setup_ui(self):
        # 上方按钮布局：添加矩阵 ， 删除当前矩阵
        tmp_layout = QHBoxLayout()
        self.add_matrix_button = QPushButton("添加矩阵", self)
        self.delete_matrix_button = QPushButton("删除当前", self)
        tmp_layout.addWidget(self.add_matrix_button)
        tmp_layout.addWidget(self.delete_matrix_button)
        self.main_layout_QVBoxLayout.addLayout(tmp_layout)

        # 连接按钮事件
        self.add_matrix_button.clicked.connect(self.add_matrix_dialog)
        self.delete_matrix_button.clicked.connect(self.delete_current_matrix)

        # 标签页
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setFixedHeight(500)
        self.main_layout_QVBoxLayout.addWidget(self.tab_widget)

        # 公式输入布局
        formula_layout = QHBoxLayout()
        self.formula_input = QLineEdit(self)
        self.formula_input.setPlaceholderText("输入公式，例如 |A| * B")
        self.evaluate_button = QPushButton("执行", self)
        self.evaluate_button.clicked.connect(self.evaluate_formula)
        formula_layout.addWidget(QLabel("公式:"))
        formula_layout.addWidget(self.formula_input)
        formula_layout.addWidget(self.evaluate_button)
        self.main_layout_QVBoxLayout.addLayout(formula_layout)

        # QWebEngineView 用于显示 LaTeX 结果
        self.result_QWebEngineView = QWebEngineView(self)
        self.result_QWebEngineView.setHtml(
            html_template.format(content="$$ \\text{准备就绪} $$")
        )
        self.main_layout_QVBoxLayout.addWidget(self.result_QWebEngineView)

    def add_matrix_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("添加矩阵")
        layout = QFormLayout(dialog)

        name_input = QLineEdit(dialog)
        rows_input = QSpinBox(dialog)
        rows_input.setRange(1, 10)
        cols_input = QSpinBox(dialog)
        cols_input.setRange(1, 10)

        layout.addRow("矩阵名:", name_input)
        layout.addRow("行数:", rows_input)
        layout.addRow("列数:", cols_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, parent=dialog)
        layout.addWidget(buttons)

        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)

        if dialog.exec() == QDialog.Accepted:
            name = name_input.text().strip()
            rows = rows_input.value()
            cols = cols_input.value()
            if not name:
                QMessageBox.warning(self, "错误", "矩阵名不能为空")
                return
            try:
                self.backend.add_matrix(name, rows, cols)
                self.add_matrix_tab(name, rows, cols)
            except ValueError as e:
                QMessageBox.warning(self, "错误", str(e))

    def add_matrix_tab(self, name: str, rows: int, cols: int):
        table = QTableWidget(rows, cols, self)
        table.setHorizontalHeaderLabels([f"列 {i+1}" for i in range(cols)])
        table.setVerticalHeaderLabels([f"行 {i+1}" for i in range(rows)])
        table.cellChanged.connect(lambda r, c: self.update_matrix(name, r, c, table.item(r, c).text()))
        self.tab_widget.addTab(table, name)

    def update_matrix(self, name: str, row: int, col: int, value: str):
        try:
            self.backend.set_element(name, row, col, value)
        except ValueError as e:
            QMessageBox.warning(self, "错误", str(e))

    def delete_current_matrix(self):
        current_index = self.tab_widget.currentIndex()
        if current_index == -1:
            QMessageBox.warning(self, "错误", "没有选中的矩阵")
            return
        name = self.tab_widget.tabText(current_index)
        try:
            self.backend.remove_matrix(name)
            self.tab_widget.removeTab(current_index)
        except ValueError as e:
            QMessageBox.warning(self, "错误", str(e))

    def evaluate_formula(self):
        formula = self.formula_input.text().strip()
        if not formula:
            QMessageBox.warning(self, "错误", "公式不能为空")
            return
        try:
            result = self.backend.perform_operation(formula)
            result_latex = sympy.latex(result)
            # 将 matrix 环境替换为 pmatrix
            result_latex = result_latex.replace(r'\begin{matrix}', r'\begin{pmatrix}')
            result_latex = result_latex.replace(r'\end{matrix}', r'\end{pmatrix}')
            self.update_result(result_latex)
        except ValueError as e:
            QMessageBox.warning(self, "错误", str(e))

    def update_result(self, latex_str: str):
        """更新显示结果的统一接口，直接把 LaTeX 源码输出到 QWebEngineView"""
        html_content = html_template.format(content=f"$$ {latex_str} $$")
        self.result_QWebEngineView.setHtml(html_content)