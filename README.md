# superimport
Simple package to lookup missing packages and autoinstall them.
## Installing using PyPi:
`pip install superimport`
## Usage:
There are two ways to use superimport:

- superimport can be called as a program, see `-h` for args. This allows you to do "superimports" across mulitple files and folders.
- by adding `import superimport` to the top of your python script. This is the per script mode.
## Examples:
See this notebook 



<a href="https://colab.research.google.com/github/probml/probml-notebooks/blob/main/notebooks/Superimport.ipynb" target="_parent">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


## 🔪 Sharp edges 🔪:
- If the missing python package contains a requirement that is not listed in its own requirements.txt and is being used your file will fail anyway.
- If you import superimport twice in the same process (a common usecase is ipython kernels), the second time will not work because of the way python [loads modules](https://docs.python.org/3/reference/import.html) , you would need a something like [deimport](https://github.com/probml/deimport) to deimport the package before being able to import superimport to the desired effect again.
- If you run superimport in ipython, please use [deimport](https://github.com/probml/deimport/) to deimport superimport and use `%run -n` if you use `%run`
