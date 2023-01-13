import numpy as np 

arr= np.array(
    [1,2,4]
)

print(arr, type(arr))
print("Shape of the array: ", arr.shape)

# arr2D = np.array([
#     [2,3],
#     [5,6],
#     [6,7]
# ])

# print(arr2D,  arr2D.shape)
# print(arr2D[0][1], arr2D[1][1])

# arr3D = np.array(
#     [
#     [[3,4,5],
#     [5,6,7],
#     [8,3,7],
#     ],
#     [
#     [5,6,7],
#     [4,2,3],
#     [3,6,9],
#     ],
#     [
#     [5,6,7],
#     [6,8,9],
#     [9,5,4]
#     ]
#     ]
# )

# print(arr3D[0,0,0])
# print(arr3D[0])
# print(arr3D[0,0])

zeros = np.zeros((4,5))
print(zeros)

ones = np.ones((3,3,3))
print(ones)


