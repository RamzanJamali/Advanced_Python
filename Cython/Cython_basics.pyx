# To run this code use ipython. 
# 1. %load_ext Cython
# 2. %%cython
# 3. paste your cython code
# 4. alt + enter

# Declaring variables in cython.
cdef int i
i = 0

# Declaring multiple variables in single line
cdef double a, b = 2.0

# print(a, b, i)


# Checking performance of declaring variables in cython
def example_cython():
    cdef int i, j = 0
    for i in range(100):
        j += 1

    return j
# %timeit example_cython()

# Same thing in python
def example_python():
    j = 0
    for i in range(100):
        j += 1

    return j
# %timeit example_python()

# creating objects in python
cdef object a_py
# both 'hello' and 1 are python objects
a_py = 'hello'
a_py = 1

# changing type of variable in cython
cdef int a = 0
cdef double b
b = <double> a


# Defining functions 
# with type information

# first in python
def max_python(int a, int b):
    return a if a>b else b

# now in cython (cannot be called in python)
cdef int max_cython(int a, int b):
    return a if a>b else b

# declaring same function to call it from both python and cython
# it generates two versions, one slower for python interpreter and second fast for c.
cpdef int max_hybrid(int a, int b):
    return a if a>b else b

# writing small functions in inline so that it can be efficient when calling multiple times
cdef inline int max_inline(int a, int b):
    return a if a>b else b


# Declaring Class in cython
cdef class Point:
    cdef double x
    cdef double y
    def __init__ (self, double x, double y):
        self.x = x
        self.y = y

cdef double norm(Point p):
    return (p.x**2 + p.y**2)**0.5

# making object from class
point_a = Point(2, 5)
# Using class and function
print(norm(point_a))

# This will generate attribute error
a = Point(0.0, 0.0)
a.x

# To access attributes from python code we use 'public' or 'readonly' specifiers
cdef class Point:
    cdef public double x
    cdef public double y
    def __init__ (self, double x, double y):
        self.x = x
        self.y = y

# Now it will not attribute error
a = Point(0.0, 0.0)
a.x