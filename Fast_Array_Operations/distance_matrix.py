import numpy as np
import numexpr as ne

def distance_matrix_numpy(n):
    r = np.random.rand(n, 2)
    r_i = r[:, np.newaxis]
    r_j = r[np.newaxis, :]
    d_ij = r_j - r_i

    return np.sqrt((d_ij ** 2).sum(axis=2))


def distance_matrix_numexpr(n):
    r = np.random.rand(n, 2)
    r_i = r[:, np.newaxis]
    r_j = r[np.newaxis, :]
    d_ij = ne.evaluate("sum((r_j - r_i)**2, 2)")

    return ne.evaluate("sqrt(d_ij)")


if __name__ == '__main__':

    import cProfile
    cProfile.run('distance_matrix_numexpr(10000)')
    cProfile.run('distance_matrix_numpy(10000)')