import pathlib
from setuptools import setup, find_packages

# The directory containing this file
with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = "0.1"
DESCRIPTION = "This is a test file"
setup(
    name ="ABIR10",
    version = VERSION,
    description = DESCRIPTION,
    long_description = long_description,
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
