from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as f:
    description = f.read()

with open("LICENSE", "r") as f:
    license = f.readline()

setup(
    name="sRemoAPI",
    version="1.0.0",
    author="zunda(@zunda_pixel)",
    author_email="zunda.pixel@gmail.com",
    description="Python client for sRemo(sCloud) API",
    url="https://github.com/zunda-pixel/sRemo",
    long_description=description,
    long_description_content_type="text/markdown",
    license=license,
    packages=find_packages(exclude="sRemo")
)
