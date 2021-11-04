import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='abir',  
     version='0.1',
     scripts=['abir'] ,
     author="ABIR HOSSAIN",
     author_email="abirhossain200019@gmail.com",
     description="this is a test file",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/ABIRHOSSAIN10/test",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
