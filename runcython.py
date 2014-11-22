from distutils.core import setup
from Cython.Build import cythonize
import os, sys, time

progname = ""

if len(sys.argv)==2:
    progname = sys.argv[1]
    print("Running Program:", progname) 
else:
    print("Usage: python runcython.py modulename")
    sys.exit()

module = os.path.splitext(os.path.basename(progname))[0]
exec "import "+module
exec "functions = dir("+module+")"
funcs = [f for f in functions if f[:2] != "__"]
print ("Implemented functions:", funcs)

if "main" in funcs:
    start_time = time.clock()
    exec module+".main()"
    print time.clock() - start_time, "seconds execution time."
