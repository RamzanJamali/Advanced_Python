
# This code defines a generator function "range_generator()" that yields a sequence of integers from 0 up to 'n-1'. 
# The generator function is called with an argument of 3, creating a generator object. 
# The first two values from the generator object are retrieved using the "next()" function and printed to the console.

def range_generator(n):
    i = 0
    while i < n:
        print("Generating value {}".format(i))
        yield i
        i += 1


if __name__ == "__main__":
    generator = range_generator(3)
    print(generator)

    next(generator)

    next(generator)