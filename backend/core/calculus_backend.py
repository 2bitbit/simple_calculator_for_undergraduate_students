import sympy


class CalculusBackend:
    def __init__(self):
        self.variables = []  # 存储已有的变量
        self.init_variables()

    def update_variable_names_list(self, lst: list[str]):
        """更新变量名字列表为lst，并初始化变量"""
        self.variables = lst
        for name in self.variables:
            setattr(self, name, sympy.symbols(name))

    def init_variables(self):
        """初始化变量列表"""
        lst = ["x", "y", "z", "n"]
        self.update_variable_names_list(lst)

    def add_variable(self, lst: list[str]):
        """添加变量"""
        lst = self.variables + lst
        self.update_variable_names_list(lst)

    def remove_variable(self, to_remove_var_names: list[str]):
        """删除变量"""
        for name in to_remove_var_names:
            delattr(self, name)
        vars = self.variables[:]
        for name in to_remove_var_names:
            vars.remove(name)
        self.update_variable_names_list(vars)

    def overwrite_variable(self, var_names: list[str]):
        """覆盖变量"""
        for name in self.variables:
            delattr(self, name)
        self.update_variable_names_list(var_names)

    def differentiate(self, expr: sympy.Expr, var_name: str, order: int):
        """计算导数"""
        return sympy.diff(expr, getattr(self, var_name), order)
    
    def undefinite_integrate(self, expr: sympy.Expr, var_name: str):
        """计算不定积分"""
        return sympy.integrate(expr, getattr(self, var_name))

    def definite_integrate(self, expr: sympy.Expr, var_name: str, lower_limit, upper_limit):
        """计算定积分"""
        return sympy.integrate(expr, (getattr(self, var_name), lower_limit, upper_limit))

    def taylor(self, expr: sympy.Expr, var_name: str, order: int, point: int):
        """计算泰勒展开式"""
        return sympy.series(expr, getattr(self, var_name), order, point)

