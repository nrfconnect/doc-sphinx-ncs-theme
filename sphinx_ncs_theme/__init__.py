import os


__version__ = "0.4.0"


def setup(app):
    app.add_html_theme(
        "sphinx_ncs_theme", os.path.dirname(os.path.abspath(__file__))
    )

    app.add_js_file("js/ncs.js")

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
