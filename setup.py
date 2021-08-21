from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name="superimport",
    packages=["superimport"],
    version="0.1.1a",
    license="MIT",
    description="Simple reverse lookup for the current python file missing packages",
    author="Mahmoud Soliman",
    author_email="mjs@aucegypt.edu",
    url="https://github.com/probml/superimport",
    download_url="https://github.com/probml/superimport/archive/refs/tags/v_011a.tar.gz",
    keywords=["setup", "runtime", "automation"],
    install_requires=[
        "pipreqs",
        "requests",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    include_package_data=True,
    package_data={"": ["mapping2"]},
)
