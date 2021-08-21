# superimport
Simple package to lookup missing packages and autoinstall them.
## Installing using PyPi:
`pip install superimport`
## Usage:
There are two ways to use superimport:

- superimport uses [phython](https://github.com/mjsML/phython) to hook python and lookup all imports in your current folder and make sure they are 'importable' if not it will attempt to install automatically the missing packges. This is a "global install" meaning that for every python script superimport will be invoked before the script is run to check it will have the packages it needs.
- by adding `import superimport` to the top of your pythong script. This is the per script mode.

## Limitations:
If the missing python package contains a requirement that is not listed in its own requirements.txt and is being used your file will fail anyway.
