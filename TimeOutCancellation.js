function cancellable(fn, args, t) {
    let timeout= setTimeout(()=>{fn(...args);},t);
    let cancelFn= ()=>{
        clearTimeout(timeout);
    };
    return cancelFn;
}