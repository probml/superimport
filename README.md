# superimport
Simple package to lookup missing packages and autoinstall them.
## Installing using PyPi:
`pip install superimport`
## Usage:
There are two ways to use superimport:

- superimport can be called as a program, see -h for args. This allows you to do "superimports" across mulitple files and folders.
- by adding `import superimport` to the top of your pythong script. This is the per script mode.

## Limitations:
If the missing python package contains a requirement that is not listed in its own requirements.txt and is being used your file will fail anyway.
