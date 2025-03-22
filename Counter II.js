var createCounter = function(init) {
    var resetVal=init;
    return {
        increment(){
        return ++init;
        },
        decrement(){
           return --init;
        },
        reset(){
           return init=resetVal;
        }
    };
};