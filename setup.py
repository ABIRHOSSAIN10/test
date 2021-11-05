import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

VERSION = "0.1"
DESCRIPTION = "This is a test file"
setup(
    name ="ABIR",
    version = VERSION,
    description = DESCRIPTION,
    long_description = README,
    long_description_content_type = "text/markdown",
    url = "https://github.com/ABIRHOSSAIN10/test",
    author="ABIRHOSSAIN",
    author_email = "abirhossain200019@gmail.com",

    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = find_packages(),
    include_package_data = True,
)
