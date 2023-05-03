#A factory method can improve performance and memory usage by creating new objects only if it is necessary. 
# When we create objects using a direct class instantiation, extra memory is allocated every time 
# a new object is created (unless theclass uses caching internally, which is usually not the case).

class A:
    pass

# This creates two instances of the same class, A, and uses the id() function to compare their 
# memory addresses. These addresses are also printed in the output so that we can inspect them. 
# The fact that the memory addresses are different means that two distinct objects are created.

if __name__ == '__main__':
    a = A()
    b = A()
    print(id(a) == id(b))
    print(a, b)
