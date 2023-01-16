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

print(a, b, i)