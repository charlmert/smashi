import setuptools
with open("readme.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='smashi',  
     version='1.3',
     author="Charl Joseph Mert",
     author_email="charl.mert@gmail.com",
     description="A python3 library with useful utilities",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/charlmert/smashi",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
