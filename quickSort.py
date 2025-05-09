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
