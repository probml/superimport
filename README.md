# superimport
Simple runtime lookup for missing packages.
## Installing using PyPi:
`pip install superimport`
## Usage:
superimport uses [phython](https://github.com/mjsML/phython) to hook python and lookup all imports in your current folder and make sure they are 'importable' if not it will attempt to install automatically the missing packges.

## Limitations:
If the missing python package contains a requirement that is not listed in its own requirements.txt and is being used your file will fail anyway.
