import numpy as np

# # arr = np.array([
# #     [5,4,6,7],
# #     [6,8,4,7],
# #     [4,5,8,8]
# # ])

# # print(arr, arr.shape)

# # s_arr = arr[:2, 1:3]
# # print(s_arr, s_arr.shape)

# # #Questions
# # #Extract last row and col 0, col1
# # #Extract second row
# # #Extract third column
# # #Extract col1 and col2

# # print(arr[-1,:2])
# # print(arr[-2,:])
# # print(arr[:, 2:3])
# # print(arr[:,1:3])

# # print(arr)
# # bool_idx= [arr > 3]
# # print(bool_idx)

# # print(arr[arr>3])


# x= np.array([
#     [2,4],
#     [5,3]
# ])
# print(x)
# y= np.array([
#     [1,2],
#     [3,5]
# ])
# print(y)
# # print(x+y)
# # print(np.add(x,y))
# # print(np.subtract(x,y))
# # print(np.multiply(x,y))
# # print(np.divide(x,y))

# # print(np.sqrt(x))

# v= np.array([4,5])
# w= np.array([3,6])

# print(v.dot(w))
# print(np.dot(v,w))

# print(x.dot(w))
# print(np.dot(x,w))


# print(x.dot(y))
# print(np.dot(x,y))

# print(x)
# print(x.T)

# u= np.array([
#     [3,0,5],
#     [6,7,3],
#     [6,8,4]
# ])

# print(u)
# print(u.T)

# print("sum of all elements of u: ", np.sum(u))
# print("sum of each column: ", np.sum(u, axis=0))
# print("sum of all rows: ", np.sum(u, axis=1))

# x= np.array([
#     [3,4,5],
#     [2,6,3],
#     [8,4,1]
# ])

# v= np.array([1,0, 1])

# # y= np.empty_like(x)
# # print(y)

# # for i in range(len(x)):
# #     y[i, :]= x[i, :] +v

# #     print(x)

# #     print(y)


# #mathematical approach

# stacked_v = np.tile(v, (3,1))

# print(stacked_v)
# print(x+v)



x= np.array([1, 2, 3])

print(x)
print(np.reshape(x, (3,1)))

x= np.array([
    [3,4,5],
    [6,2,1]
])
print(x)
print(np.reshape(x, (3,2)))