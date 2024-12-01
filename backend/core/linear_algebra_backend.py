import sympy
import re
'''此部分主要由o1-mini编写。感恩。'''

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

    def get_matrix(self, name: str) -> sympy.Matrix:
        if name not in self.matrices:
            raise ValueError(f"矩阵{name}不存在")
        return self.matrices[name]
    
    def perform_operation(self, expression: str) -> sympy.Matrix:
        """
        解析并执行矩阵运算，例如 "A + B * C"
        支持的操作包括加法、减法、乘法、转置等
        """
        # 替换矩阵名为self.matrices中的变量
        for name in self.matrices:
            expression = re.sub(r'\b{}\b'.format(re.escape(name)), f'self.matrices["{name}"]', expression)
        
        try:
            # 计算结果
            result = eval(expression, {"self": self, "sympy": sympy})
            if not isinstance(result, sympy.Matrix):
                raise ValueError("运算结果必须是一个矩阵")
            return result
        except Exception as e:
            raise ValueError(f"运算错误: {e}")
