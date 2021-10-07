import fealpy
from frogpy.algebra import matrix

a = matrix.tri_diagonal(4, 2, 1, 1)
print(a)
print(fealpy.__file__)
print(matrix.__file__)
