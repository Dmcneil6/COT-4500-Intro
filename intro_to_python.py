##________________________________

import numpy as np
matrix1 = np.eye(3)
print(matrix1)

matrix2 = np.eye(3)
matrix2[matrix2 != 1] += 3
print(matrix2)

matrix3 = np.eye(3)
matrix3[matrix3 != 1] += 3
matrix3 = np.delete(matrix3, -1, 1)
print(matrix3)