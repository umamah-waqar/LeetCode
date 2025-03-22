var map = function(arr, fn) {
    var newArr= arr;
    for(let i=0;i<arr.length;i++){
        newArr[i]=fn(arr[i],i,arr);
    }
    return newArr;
};