import numpy as np
"""

a = [[1, 2, 3], [4, 5, 6]]
b = np.array(a)
print(b)

# 배열의 크기(모양) 반환 ( 튜플 형태 )
print(np.shape(b))  # (2, 3)

# 배열의 차원을 반환
print(np.ndim(b))  # 2

# 배열의 각 원소의 자료형을 반환
print(b.dtype)  # int32

# 배열의 각 원소 하나의 크기 ( 바이트 단위 )
print(b.itemsize)  # 4

# 배열의 전체 원소 개수를 반환
print(np.size(b))  # 6
"""

"""
import numpy as np
lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
arr = np.array(lists)

a = arr[1, 2]
print(a)            ## 6    

a1 = [1, 1]
a2 = [2, 1]
print(arr[a1, a2])  ## [ 6 5 ]


a = arr[0:2, 0:1]
print(a)
# [[1]
#  [4]]


a = arr[:2, 0:3]
print(a)
# [[]]
"""


# zeros_arr = np.zeros((2, 3, 3))
# [[[0. 0. 0.]
#   [0. 0. 0.]
#   [0. 0. 0.]]
#  [[0. 0. 0.]
#   [0. 0. 0.]
#   [0. 0. 0.]]]


# # [[0. 0. 0.]
# #  [0. 0. 0.]]
# print(zeros_arr)

# ones_arr = np.ones((3, 3))


# # [[1. 1. 1.]
# #  [1. 1. 1.]]
# print(ones_arr)

# arange_arr = np.arange(1, 10, 2)
# print(arange_arr)
# #[1 3 5 7 9]

# linspace_arr = np.linspace(1, 10, num=10, retstep=True)
# print(linspace_arr)


# resized = np.resize(arr, (4, 3))
# # [[1 2 3]
# #  [4 5 6]
# #  [7 8 9]
# #  [1 2 3]]


# print(resized)

# arr = np.arange(1, 13)
# # [1 2 3 4 5 6 7 8 9 10 11 12]
# reshaped = np.reshape(arr, (-1, 3))
# # [[ 1  2  3]
# #  [ 4  5  6]
# #  [ 7  8  9]
# #  [10 11 12]]

# print(reshaped)


a = np.array([1, 2, 3])
b = np.array(5)

print(a + b)  # [6 7 8]

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([2, 3, 4])

print(a + b)  # [[3 5 7] [6 8 10]]
