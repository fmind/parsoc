#!/usr/bin/env python3

import setuptools  # type: ignore

META = dict(
    name="parsoc",
    version="0.1.0",
    description="Convert docx files to json",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fmind/parsoc",
    author="Médéric Hurier (fmind)",
    author_email="fmind@fmind.me",
    license="LGPL-3.0",
    packages=["parsoc"],
    keywords="docx json parse convert",
    classifiers=["Development Status :: 4 - Beta"],
    entry_points={"console_scripts": ["parsoc=parsoc.__main__:main"]},
    python_requires=">=3.7",
    install_requires=[
        "python-docx",
    ],
)

if __name__ == "__main__":
    setuptools.setup(**META)
