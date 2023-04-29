import theano.tensor as T
import theano as th


a = T.scalar('a')
a_sq = a ** 2
print(a_sq)

computer_square = th.function([a], a_sq)
computer_square(2)

a = T.vector('a')
b = T.vector('b')

ab_sq = a**2 + b**2
computer_square = th.function([a, b], ab_sq)

computer_square([0, 1, 2], [3, 4, 5])