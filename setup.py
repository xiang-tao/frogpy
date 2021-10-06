from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dinosaur",  # This is the name of the package
    version="0.0.1",  # The initial release version
    author="Tao Xiang",  # Full name of the author
    url = "https://github.com/xiang-tao/dragon",
    author_email="xiangtao@smail.xtu.edu.cn",
    description="dinosaur:Solve equations and design algorithms",
    long_description=long_description,  # Long description read from the the readme file
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)
