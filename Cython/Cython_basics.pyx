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