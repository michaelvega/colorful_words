import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "readme.MD").read_text()

# This call to setup() does all the work
setup(
    name="colorful_words",
    version="1.0.0",
    description="Package adds many functionalities related to outputting text and logs in color.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/michaelvega/colorful_words",
    author="Michael Vega",
    license="MIT",
    classifiers=[
        "License :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["ColorfulWords"],
    include_package_data=True,
    install_requires=["certifi", "charset-normalizer", "feedparser", "html2text", "idna", "nose", "PyYAML", "Random-Word", "requests", "sgmllib3k", "urllib3"],
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)