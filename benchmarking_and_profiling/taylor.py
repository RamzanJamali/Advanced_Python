# Use this link to download KCachegrind for windows
#  http://sourceforge.net/projects/qcachegrindwin/

def factorial(n):
    if n == 0:
        return 1.0
    else:
        return n * factorial(n-1)


def taylor_exp(n):
    return [1.0/factorial(i) for i in range(n)]


def taylor_sin(n):
    res = []
    for i in range(n):
        if i % 2 == 1:
            res.append((-1)**((i-1)/2) / float(factorial(i)))

        else:
            res.append(0.0)

    return res


def benchmark():
    taylor_exp(500)
    taylor_sin(500)


if __name__ == '__main__':
    benchmark()

# First we need to generate cProfile output file, as follows (on commmand line):
# python -m cProfile -o prof.out taylor.py
# Then run following commands
# pyprof2calltree -i prof.out -o prof.calltree
# kcachegrind prof.calltree # or qcachegrind prof.calltree

# if the above command does not work then download qcachegrind program and run scripts manually