from distutils.core import setup
from Cython.Build import cythonize
import sys

projname = ""
progname = ""
if len(sys.argv)>2:
    projname = sys.argv[1]
    print("Found Project name:", projname)
    progname = sys.argv[2]
    print("Found Program name:", projname)
elif len(sys.argv)==2:
    projname = progname = sys.argv[1]
    print("Found Program name", progname, "which is project name at the same time.") 
try:
    sys.argv[1] = "build_ext"
except:
    sys.argv.append("build_ext")
try:
    sys.argv[2] = "--inplace"
except:
    sys.argv.append("--inplace")
setup(
    name = projname,
    ext_modules = cythonize(progname), # accepts a glob pattern
)