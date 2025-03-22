var reduce = function(nums, fn, init) {
    if(nums.length==0){
        return init;
    }
    let newVal=fn(init,nums[0])
    for(let i=1;i<nums.length;i++){
        newVal=fn(newVal,nums[i]);
    }
    return newVal;
};