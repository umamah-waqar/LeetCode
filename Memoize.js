function memoize(fn) {
    let ans = {};  
    return function(...args) {
        const key = JSON.stringify(args); 
        if (key in ans){ 
            return ans[key]; 
        }  else{
            const result = fn(...args);
            ans[key] = result; 
            return result;
        }
    };
}