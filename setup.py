from setuptools import setup
import re
import os.path


CURDIR = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(CURDIR, "sphinx_ncs_theme", "__init__.py")) as f:
    VERSION = re.search(r'__version__\s+=\s+"(.*)"', f.read()).group(1)

with open(os.path.join(CURDIR, "requirements.txt")) as requirements:
    REQUIREMENTS = requirements.read().splitlines()


setup(
    name="sphinx-ncs-theme",
    version=VERSION,
    url="https://www.nordicsemi.no",
    author="Nordic Semiconductor ASA",
    packages=["sphinx_ncs_theme"],
    license="MIT",
    description="Nordic Semiconductor NCS theme for Sphinx",
    long_description=open("README.rst", encoding="utf-8").read(),
    package_data={
        "sphinx_ncs_theme": [
            "theme.conf",
            "*.html",
            "static/**/*",
        ]
    },
    include_package_data=True,
    entry_points={
        "sphinx.html_themes": [
            "sphinx_ncs_theme = sphinx_ncs_theme",
        ]
    },
    install_requires=REQUIREMENTS,
    classifiers=[
        "Framework :: Sphinx",
        "Framework :: Sphinx :: Theme",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
    ],
)
