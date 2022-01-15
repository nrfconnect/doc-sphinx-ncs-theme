import os

import sphinx_book_theme


__version__ = "0.7.0"


def setup(app):
    sphinx_book_theme.setup(app)

    app.add_html_theme(
        "sphinx_ncs_theme", os.path.dirname(os.path.abspath(__file__))
    )

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
