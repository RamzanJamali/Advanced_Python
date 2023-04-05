from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize


hello_parallel = Extension(
    "hello_parallel",
    ["hello_parallel.pyx"],
    extra_compile_args=['-openmp'],
    extra_link_args=['-openmp'],
)

cevolve = Extension(
    "cevolve",
    ["cevolve.pyx"],
    extra_compile_args=['-openmp'],
    extra_link_args=['-openmp'],
)


setup(
    name="Hello",
    ext_modules=cythonize([cevolve, hello_parallel]),
)

# Navigate to setup.py directory and run following command
# python setup.py install