import sys
from superimport import superimport
system=sys.version_info
if system[0]==3 and system[1]>=9:
    from superimport.superimport import *
