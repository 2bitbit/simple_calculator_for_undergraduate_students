from utils import PATHS

html_template = """
<!DOCTYPE html>
<html>
<head>
    <script>
       MathJax = {{{{
            loader: {{{{
                load: [
                    "input/tex",
                    "output/chtml",
                ],
            }}}},
            tex: {{{{
                inlineMath: [
                    ["$", "$"],
                ],
                displayMath: [
                    ["$$", "$$"],
                ],
                packages: ["base", "ams"],
            }}}},
        }}}};
    </script>
    <script id="MathJax-script" async
        src="{mathjax_path}">
    </script>
    <style>
        body {{{{
            background-color: #008000;
            font-size: 24px;
            padding: 20px;
        }}}};
    </style>
</head>
<body>
    <div>{{content}}</div>
</body>
</html>
""".format(mathjax_path=PATHS["mathjax_path"])
