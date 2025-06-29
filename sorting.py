def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

def insertionSort(arr):
    for i in range(len(arr)):
        j=i-1
        val=arr[i]
        while(j>=0 and val<arr[j]):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=val

def mergeSort(arr,left,right):
    if(left>=right):
        return [arr[left]]
    mid=left+right//2
    res1=mergeSort(arr,left,mid)
    res2=mergeSort(arr,mid+1,right)
    return merge(res1,res2)
def merge(left, right):
    temp =[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            temp.append(left[i])
            i=i+1
        else:
            temp.append(right[j])
            j=j+1
    while i < len(left):
        temp.append(left[i])
        i=i+1
    while j < len(right):
        temp.append(right[j])
        j=j+1

def quickSort(arr,pivotindex,p,q):
    if p>=q:
        return
    pivot=arr[pivotindex] 
    while True:
        while p<=q and arr[p]<pivot:
            p+=1
        while p<=q and arr[q]>pivot:
            q-=1
        if p<q:
            arr[p],arr[q]= arr[q],arr[p]
        else: 
            arr[pivotindex],arr[q]=arr[q],arr[pivotindex]
            break
    quickSort(arr,pivot,pivot+1,q-1) 
    quickSort(arr,q+1,q+2,n-2)

arr=[2,3,6,1,4,9,5,10] 
n=len(arr)
quickSort(arr,0,1,n-2)
print(arr)



        
