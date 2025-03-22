var once = function(fn) {
    let check=false; 
    return function(...args) {
        if (!check) {
            check=true; 
            return fn(...args); 
        }
        return undefined;
    };
};