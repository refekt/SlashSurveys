import io
import os

from setuptools import setup

NAME = "discord-surveys"
DESCRIPTION = "A survey object that utilizes discord.py and discord-interactions."
URL = "https://github.com/refekt/discord-surveys"
EMAIL = "refekt@gmail.com"
AUTHOR = "refekt"
REQUIRES_PYTHON = ">=3.7.0"
VERSION = "1.0.5"

REQUIRED = [
    "discord-py-interactions==3.0.2",
    "discord==1.7.3"
]

EXTRAS = {
    # "fancy feature": ["django"],
}

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    py_modules=["SlashSurveys"],
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
