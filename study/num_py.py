import numpy as np
"""
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.hstack([a, b])) # [1 2 3 4 5 6]
print(np.vstack([a, b])) # [[1 2 3]
                         #  [4 5 6]]

print(np.column_stack([a, b]))
# [[1 4]
#  [2 5]
#  [3 6]]

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(np.hsplit(a, 2))
#[array([[1, 2],
#        [5, 6]]),
# array([[3, 4],
#        [7, 8]])]

print(np.vsplit(a, 2))
# [array([[1, 2, 3, 4]]),
#  array([[5, 6, 7, 8]])]






# print(a+b) # [5 7 9]
# print(a-b) # [-3 -3 -3]
# print(a*b) # [4 10 18]
# print(a/b) # [0.25 0.4 0.5]

# a = np.array([1, 4, 9, 16, 25, 36])

# # 제곱근
# print(np.sqrt(a))

# print()
# # 지수함수
# print(np.exp(a))
"""

a = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
b = np.array([[1], [2], [3]])

print(a.shape) # (3,)
print(b.shape) # (3, 1)

print(a + b)
# [[2 3 4]
#  [3 4 5]
#  [4 5 6]]