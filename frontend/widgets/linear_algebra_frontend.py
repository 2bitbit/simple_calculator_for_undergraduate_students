from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QLineEdit,
    QMessageBox,
    QLabel,
    QDialog,
    QFormLayout,
    QDialogButtonBox,
    QSpinBox,
)
from PySide6.QtCore import Qt
from PySide6.QtWebEngineWidgets import QWebEngineView
from backend.core.linear_algebra_backend import LinearAlgebraBackend
import sympy
from frontend.html_template import html_template


class LinearAlgebraFrontend(QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        self.backend = LinearAlgebraBackend()
        self.main_layout_QVBoxLayout = QVBoxLayout(self)
        self.setup_ui()

    def setup_ui(self):
        # 添加矩阵的按钮，删除当前矩阵的按钮
        tmp_layout = QHBoxLayout()
        self.main_layout_QVBoxLayout.addLayout(tmp_layout)

        self.add_matrix_button = QPushButton("添加矩阵", self)
        self.add_matrix_button.clicked.connect(self.add_matrix_dialog)
        tmp_layout.addWidget(self.add_matrix_button)

        self.delete_matrix_button = QPushButton("删除当前矩阵", self)
        self.delete_matrix_button.clicked.connect(self.delete_current_matrix)
        tmp_layout.addWidget(self.delete_matrix_button)

        # 标签页
        self.tab_QTabWidget = QTabWidget(self)
        self.tab_QTabWidget.setFixedHeight(300)
        self.main_layout_QVBoxLayout.addWidget(self.tab_QTabWidget)

        # 公式输入小贴士
        tmp_QLabel = QLabel(
            "数乘，矩阵乘法：用*；转置：用^T连接；行列式：用|A|表示；求特征值和特征向量：eigen(...);特征多项式：charpoly(...);",
            self,
        )
        tmp_QLabel.setFixedHeight(20)
        self.main_layout_QVBoxLayout.addWidget(tmp_QLabel)

        # 公式输入
        tmp_layout = QHBoxLayout()
        self.main_layout_QVBoxLayout.addLayout(tmp_layout)

        self.formula_QLineEdit = QLineEdit(self)
        self.formula_QLineEdit.setPlaceholderText("输入公式，例如 |A|*(B^T*C)")
        self.formula_QLineEdit.returnPressed.connect(self.evaluate_formula)
        tmp_layout.addWidget(self.formula_QLineEdit)

        self.evaluate_QPushButton = QPushButton("执行", self)
        self.evaluate_QPushButton.clicked.connect(self.evaluate_formula)
        tmp_layout.addWidget(self.evaluate_QPushButton)

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

        name_input_QLineEdit = QLineEdit(dialog)
        rows_input_QSpinBox = QSpinBox(dialog)
        rows_input_QSpinBox.setRange(1, 10)
        cols_input_QSpinBox = QSpinBox(dialog)
        cols_input_QSpinBox.setRange(1, 10)

        layout.addRow("矩阵名:", name_input_QLineEdit)
        layout.addRow("行数:", rows_input_QSpinBox)
        layout.addRow("列数:", cols_input_QSpinBox)

        # "创建"按钮以及"取消创建"按钮
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel, parent=dialog
        )
        layout.addWidget(buttons)

        def handle_dialog_accepted():
            name = name_input_QLineEdit.text().strip()
            rows = rows_input_QSpinBox.value()
            cols = cols_input_QSpinBox.value()
            if not name:
                QMessageBox.warning(self, "错误", "矩阵名不能为空")
                return
            try:
                self.backend.add_matrix(name, rows, cols)
                self.add_matrix_tab(name, rows, cols)
                dialog.accept()
            except ValueError as e:
                QMessageBox.warning(self, "错误", str(e))
                return

        def handle_dialog_rejected():
            dialog.reject()

        buttons.accepted.connect(handle_dialog_accepted)
        buttons.rejected.connect(handle_dialog_rejected)

        dialog.exec()

    def add_matrix_tab(self, name: str, rows: int, cols: int):
        table = QTableWidget(rows, cols, self)
        table.setHorizontalHeaderLabels([f"列 {i+1}" for i in range(cols)])
        table.setVerticalHeaderLabels([f"行 {i+1}" for i in range(rows)])
        table.cellChanged.connect(
            lambda r, c: self.update_matrix(name, r, c, table.item(r, c).text())
        )
        self.tab_QTabWidget.addTab(table, name)

    def update_matrix(self, name: str, row: int, col: int, value: str):
        try:
            self.backend.set_element(name, row, col, value)
        except ValueError as e:
            QMessageBox.warning(self, "错误", str(e))

    def delete_current_matrix(self):
        current_index = self.tab_QTabWidget.currentIndex()
        if current_index == -1:
            QMessageBox.warning(self, "错误", "没有选中的矩阵")
            return
        name = self.tab_QTabWidget.tabText(current_index)
        try:
            self.backend.remove_matrix(name)
            self.tab_QTabWidget.removeTab(current_index)
        except ValueError as e:
            QMessageBox.warning(self, "错误", str(e))

    def evaluate_formula(self):
        formula = self.formula_QLineEdit.text().strip()
        if not formula:
            QMessageBox.warning(
                self, "你发动了：无量空处！！", "没有公式的话，会执行成功的"
            )
            return
        try:
            # 执行运算
            result = self.backend.perform_operation(formula)

            # 处理返回结果，使之称为字符串
            if isinstance(result, tuple):  # 求特征值和特征向量时会返回元组
                result_latex = (
                    r"\begin{align}"
                    + sympy.latex(result[0]).replace(r"(^\{)|(\}$)","").replace(r":", r"重数：")
                    + r"\\"
                    + sympy.latex(result[1]).replace(r"{matrix}", r"{pmatrix}")
                    + r"\end{align}"
                )
            else:
                result_latex = sympy.latex(result)
                result_latex = result_latex.replace(r"{matrix}", r"{pmatrix}")

            # 统一处理，删除多余的括号
            result_latex = result_latex.replace(r"\left[", "")
            result_latex = result_latex.replace(r"\right]", "")

            # 更新显示结果
            self.update_result(result_latex)
        except ValueError as e:
            QMessageBox.warning(self, "错误", str(e))

    def update_result(self, content: str):
        """更新显示结果的统一接口，直接把 content 原文输出到 QWebEngineView"""
        html_content = html_template.format(content=f"$$ {content} $$")
        self.result_QWebEngineView.setHtml(html_content)
