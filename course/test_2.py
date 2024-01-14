import intvalpy as ip
from intvalpy import Interval

A = ip.Interval([
    [[7, 7], [1.25, 1.25], [0, 0], [0, 0]],
    [[1.25, 1.25], [14, 14], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [7, 7], [1.25, 1.25]],
    [[0, 0], [0, 0], [1.25, 1.25], [14, 14]]
])
# b = ip.Interval([
#     [-1, -1],
#     [-2, -2],
#     [1, 1],
#     [2, 2]
# ])
#
b = ip.Interval([
    [[-1, -1]],
    [[-2, -2]],
    [[1, 1]],
    [[2, 2]]
])
#
# print(ip.linear.Gauss(A, b))

ip.linear.Gauss(A, b)