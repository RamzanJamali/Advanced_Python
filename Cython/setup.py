from distutils.core import setup 
from Cython.Build import cythonize

setup(
    name='Cython_Basics',
    ext_modules = cythonize('Cython_Basics.pyx')
)