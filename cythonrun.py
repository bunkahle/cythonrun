import os, sys

projname = ""
progname = ""
if len(sys.argv)>2:
    projname = sys.argv[1]
    # print("Found Project name:", projname)
    progname = sys.argv[2]
    # print("Found Program name:", projname)
elif len(sys.argv)==2:
    projname = progname = sys.argv[1]
    # print("Found Program name", progname, "which is project name at the same time.") 

os.system('"makecython.py '+projname+' '+progname+'"')
os.system('"runcython.py '+progname+'"')
