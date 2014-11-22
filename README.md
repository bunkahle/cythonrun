Cython is a superset of python that adds support for blazing fast c/c++ functions. 
cythonrun lets you compile and run cython files in one line. Windows, OSX and Linux are supported.

<h2>Installation</h2>

Clone or download the github repository and run the setup by entering:

    $ python setup.py install

Alternatively you can also install the package via pip:

    $ pip install cythonrun

You can now call the three scripts `cythonrun.py`, `makecython.py` and `runcython.py` in every directory.

<h2>Usage</h2>

    # hello.pyx
    def main():
        print 'hello, world'

<p>You can use python cythonrun.py directly for compiling and running the pyx-file in one go.<br>
Or you can use makecython.py just for compiling the executable and run it aftewards with runcython.py.
You should only make sure that you have a main() function definition in your pyx-file to let the
runcython.py program know where to start the execution of the code.
</p>


    $ python cythonrun.py hello.pyx
    ('Found Project name:', 'hello.pyx')
    ('Found Program name:', 'hello.pyx')
    Compiling hello.pyx because it changed.
    Cythonizing hello.pyx
    running build_ext
    building 'hello' extension
    creating build
    creating build\temp.win32-2.7
    creating build\temp.win32-2.7\Release
    c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\cl.exe /c /nologo /Ox 
    /MD /W3 /GS- /DNDEBUG -IC:\Python27\include -IC:\Python27\PC /Tchello.c /Fobuild 
    \temp.win32-2.7\Release\hello.obj hello.c
    :\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\link.exe /DLL /nologo 
    /INCREMENTAL:NO /LIBPATH:C:\Python27\libs /LIBPATH:C:\Python27\PCbuild /EXPORT:i 
    nithello build\temp.win32-2.7\Release\hello.obj /OUT:C:\Python27\Programme\Cython
    \cythonrun\hello.pyd /IMPLIB:build\temp.win32-2.7\Release\hello.lib /MANIFESTFILE:
    build\temp.win32-2.7\Release\hello.pyd.manifest
    Bibliothek "build\temp.win32-2.7\Release\hello.lib" und Objekt "build\temp.win32-
    2.7\Release\hello.exp" werden erstellt.
    ('Running Program:', 'hello.pyx')
    hello, world
    
 You can use `python cythonrun.py file.pyx` just like you would use `python file.py`.<br>
 The difference is that cythonrun.py will run a file with arbitrary cython code.
  
    # accum.pyx
    def main():
        cdef int i, n, accum
        accum = 0
        n = 10**7
        for i in range(n):
            accum += i
        print i
    main()

<p></p>

    $ python cythonrun.py accum.pyx
    ('Found Project name:', 'accum.pyx')
    ('Found Program name:', 'accum.pyx')
    running build_ext
    ('Running Program:', 'accum.pyx')
    9999999
    ('Implemented functions:', ['main'])
    9999999
    0.0161808932649 seconds execution time.
   
  There's no need to muck around with distutils or intermediate files. Using cython the typical way would require creating 5 distinct files, `accum.pyx`, `accum.c`, `accum.pyd`, `setup.py`, and `use.py`. That's a lot of moving parts to keep track of. `cythonrun.py` keeps things simple so that you can just focus on writing fast code. If you want to output a module for use in your other python files, you can always use `makecython.py` instead. If the code has already been compiled you can use `runcython.py` just for executing/testing the compiled module. Make sure you have main() definition inside your module as an entry point for `runcython.py`.

  There are some sample files in the repository (`accum.py(x)`, `circle.py(x)` and `hello.pyx`) for your convenience to test and compare cython compiled modules in one go against the pure python modules.
