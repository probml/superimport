
   
import time
import sys
start = time.time()


import superimport

import GPyOpt
import numpy
import tqdm
end = time.time()
print(end - start)


start = time.time()


g=[gl for gl in globals() if gl.startswith("super")]
s=[gl for gl in sys.modules if gl.startswith("super")]

superimport.unimport(superimport,verbose=True)


import superimport
g=[gl for gl in globals() if gl.startswith("super")]
s=[gl for gl in sys.modules if gl.startswith("super")]

end = time.time()


print(end - start)