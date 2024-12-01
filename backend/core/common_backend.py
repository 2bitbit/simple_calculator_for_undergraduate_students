import sympy

def output_process(result: sympy.Expr) -> str:
    """处理数学表达式：简化表达式并转换为 LaTeX 源码字符串

    Args:
        result: SymPy 表达式对象
    Returns:
        str: 经过简化并转换的 LaTeX 源码字符串。
    """
    result = result.subs("e", sympy.E)  # 替换 'e' 为 sympy.E
    result = sympy.expand_log(result, force=True)
    result = sympy.simplify(result)
    latex_str = sympy.latex(result)
    latex_str = latex_str.replace(r"\log", r"\ln")
    return latex_str
