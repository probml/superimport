# superimport
Simple reverse lookup for the current python file missing packages
## Installing using PyPi:
`pip install superimport`
## Usage:
```python
import superimport
```

##Limitations:
If the missing python package contains a requirement that is not listed in its own requirements.txt and is being used your file will fail anyway.
