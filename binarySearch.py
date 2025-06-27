def binarySearch(left,right,arr,key):
    if(left>right):
        return -1
    middle=(left+right)//2
    if(arr[middle]==key):
        return middle
    elif (key<arr[middle]):
        return binarySearch(left,middle-1,arr,key)
    else:
        return binarySearch(middle+1,right,arr,key)

arr=[1,2,3,4,5,6,7,8]
key=3
left=0
right=len(arr)
ans=binarySearch(left,right,arr,key)
print("Key at Index:",ans)



