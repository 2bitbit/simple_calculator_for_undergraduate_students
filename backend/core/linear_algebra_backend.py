import sympy
import re


class LinearAlgebraBackend:
    def __init__(self):
        self.matrices = {}  # 存储矩阵，键为矩阵名，值为sympy.Matrix对象

    def add_matrix(self, name: str, rows: int, cols: int):
        if name in self.matrices:
            raise ValueError(f"矩阵{name}已经存在")
        self.matrices[name] = sympy.Matrix(rows, cols, lambda i, j: 0)

    def remove_matrix(self, name: str):
        if name not in self.matrices:
            raise ValueError(f"矩阵{name}不存在")
        del self.matrices[name]

    def set_element(self, name: str, row: int, col: int, value: str):
        if name not in self.matrices:
            raise ValueError(f"矩阵{name}不存在")
        try:
            expr = sympy.sympify(value)
            self.matrices[name][row, col] = expr
        except sympy.SympifyError:
            raise ValueError(f"无效的元素值: {value}")

    def perform_operation(self, expression: str) -> sympy.Matrix:
        """执行矩阵运算，负责返回原始结果"""
        expr = self.parse_formula(expression)
        try:
            if "eigen(" in expr:  # 处理特征值和特征向量
                eigen_values = re.sub(r"eigen\((.*)\)", r"(\1).eigenvals()", expr)
                eigen_vectors = re.sub(r"eigen\((.*)\)", r"(\1).eigenvects()", expr)
                result = (
                    eval(eigen_values, {"self": self, "sympy": sympy}),
                    eval(eigen_vectors, {"self": self, "sympy": sympy}),
                )
                return result
            elif "charpoly(" in expr:  # 处理特征多项式
                lamda = sympy.symbols("lamda")  # 避免与python内置的lamda冲突。
                expr = re.sub(r"charpoly\((.*)\)", r"(\1).charpoly(lamda)", expr)
                expr = eval(
                    expr, {"self": self, "sympy": sympy, "lamda": lamda}
                ).as_expr()
                expr = sympy.factor(expr)
                return expr
            else:  # 常规计算
                result = eval(expr, {"self": self, "sympy": sympy})
                return result
        except Exception as e:
            raise ValueError(f"运算错误: {e}")

    def parse_formula(self, formula: str) -> str:
        """解析公式，返回一个可以被eval执行的字符串"""
        # 处理转置
        formula = formula.replace("^T", ".T")
        # 处理行列式
        formula = re.sub(r"\|(.*)\|", r"(\1).det()", formula)
        # 处理幂
        if "^" in formula:
            formula = re.sub(r"(.*)^(\w)", r"\1**\2", formula)
        # 将公式中的矩阵名替换为self.matrices中的变量
        for name in self.matrices:
            formula = re.sub(
                r"\b{}\b".format(re.escape(name)), f'self.matrices["{name}"]', formula
            )
        return formula
