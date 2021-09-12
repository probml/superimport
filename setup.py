# https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
# rm -rf ~/github/superimport/dist/*; python3 setup.py sdist;twine upload dist/*
from setuptools import setup
from superimport._version import __version__

setup(
    name="superimport",
    packages=["superimport"],
    version=__version__,
    license="MIT",
    description="Simple package to lookup missing packages and autoinstall them.",
    author="Mahmoud Soliman",
    author_email="mjs@aucegypt.edu",
    url="https://github.com/probml/superimport",
    download_url="https://github.com/probml/superimport/releases",
    keywords=["setup", "runtime", "automation"],
    install_requires=[
        "requests"
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
    
)
