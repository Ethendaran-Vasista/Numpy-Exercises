import numpy as np

 ary = np.array([2.5,3.6,4.7,5.8,6.9,67.1], dtype = 'int8')
# print(type(ary))
# print(ary.dtype)
# print(ary.size)
# print(ary.shape)
# print(ary.nbytes)
#
# b = np.arange(10,0,-1)
# print(b)
#
# a = np.zeros(6)
# print(a)
# c = np.ones(6)
# print(c)
# d = np.full(3,67)
# print(d)
#
# #slicing   [start:end:steps]
#
# arr = np.array([10,20,30,50,50,60,88,5,66,4,33,2,8,9,1,2,5,6,7,8,9,25,26,7,8,90])
# print(arr[0:10])
# print(arr[5:])
# print(arr[:10])
# print(arr[0:15:2])
# print(arr[5::2])
# print(arr[:20:3])
# print(arr[::2])
# print(arr[10:0:-2])
# print(arr[::-1])
# # numpy array store data homogeneous
# # internal typecasting
#
# arr = np.array(
#     [
#         [1,2,3],
#         [4,5,6],
#         [7,8,9]
#     ], dtype = "int8"
# )

#print(arr[1:2])
# print(arr[0::,::-1],"\n")
# print(arr[::-1,0::])

# print(arr.shape)
# print(arr.size)
# print(arr.ndim)
# print(arr.nbytes)

# print(arr.sum())
# print(arr.sum(axis = 1))
# print(arr.sum(axis = 0))
#
# print(arr.min(axis = 0))
# print(arr.min(axis = 1))
# print(arr.max(axis = 0))
# print(arr.max(axis = 1))

# print(arr.T)
# vert= np.vstack([arr,arr])
# hor= np.hstack([arr,arr])
# print(vert)
# print(hor)
#
# print(np.concatenate([arr,arr], axis = 0))
# print(np.concatenate([arr,arr], axis = 1))
#
# val= np.vstack([arr,arr])
# print(val)
#
#
# print(val2)
# val2= np.hstack([arr,arr])
#
#
# arr1 = np.zeros((6,7),dtype = "int")
# print(arr1)
#
# arr2 = np.ones((6,7),dtype = "int")
# print(arr2)
#
# arr3 = np.full((6,7),10,dtype = "int")
# print(arr3)
#
# a = arr.reshape(1,9)
# print(a)
#
# arr = np.arange(1,13).reshape(3,4)
# print(arr)

# result = np.where(arr % 2 == 0,67,arr)
# print(result)
#
# print(arr2[(arr2 >5) & (arr2 % 2 == 0)])
# print(arr2[(arr2 >5) | (arr2 % 2 == 0)])
# print(arr2[~(arr2 >=10) & (arr2 % 2 == 0)])
# keep
#
# arr2[2,1:] = 0
# print(arr2)

# pat = np.ones((4,5),dtype = "int")
#
# pat[1:3,1:4] = 0
# print(pat)

# 1 1 1 1 1 1 1 1 1
# 1 2 2 2 2 2 2 2 1
# 1 2 3 3 3 3 3 2 1
# 1 2 3 3 3 3 3 2 1
# 1 2 3 3 3 3 3 2 1
# 1 2 3 3 3 3 3 2 1
# 1 2 2 2 2 2 2 2 1
# 1 1 1 1 1 1 1 1 1

# patt = np.ones((8,9),dtype = "int")
# patt[1:7,1:8] = 2
# patt[2:6,2:7] = 3
# print(patt)

# arr6 = np.array([
#     [
#         [0,9,8,7,6],
#         [5,4,3,2,1],
#         [1,2,3,4,5]
#     ],
#     [
#         [4,5,6,3,2],
#         [1,3,5,6,7],
#         [2,5,7,9,1]
#     ]
# ])
# print(arr6.size)
# re = arr6.reshape(1,1,30)
#
# print(arr6)
#
# print(re)
#
# arr = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90])
#
# print(arr[5:15])
# print(arr[5:15:3])

# arr1 = np.array([3,2,1,])
# arr2 = np.array(
#     [
#         [3,4,5],
#         [6,7,8],
#         [1,4,9]
#     ]
# )
# re = np.add(arr1,arr2)
# print(re)
# arr = np.array(
# [
#  [12, 15, 18],
#  [21, 24, 27],
#  [30, 33, 36],
#  [39, 42, 45]
# ]
# )
# print(arr.size)
# print(arr.shape)
# print(arr.nbytes)
# print(arr.min())
# print(arr.max())

# arr = np.array(
# [
#  [12, 15, 18],
#  [21, 24, 27],
#  [30, 33, 36],
#  [39, 42, 45]
# ]
# )
# print(arr.sum())
# print(arr.sum(axis=1))
# print(arr.sum(axis=0))
# print(arr.flatten())

arr = np.array(
[[12, 28, 14],
 [33, 9, 5],
 [41, 6, 18]]
)
print(arr.reshape(9,1))
arr[1][1] = 900
print(arr)
arr[arr>25] = 0
print(arr)
