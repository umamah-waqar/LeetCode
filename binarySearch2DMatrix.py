def binarySearch2dMatrix(arr,key,i,j):
    if (i>len(arr) or j<0):
        return None
    if (key==arr[i][j]):
        return i,j
    elif(key>arr[i][j]):
        return binarySearch2dMatrix(arr,key,i+1,j)
    else:
        return binarySearch2dMatrix(arr,key,i,j-1)

arr = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50]
]
key = 39
i=0
j=len(arr[0])-1
x,y=binarySearch2dMatrix(arr,key,i,j)
print("Index is",x,y)



