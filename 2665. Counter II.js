/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let temp = init;
    return {
        increment: () => {
            temp++;
            return temp;
        },
        decrement: () => {
            temp--;
            return temp;
        },
        reset: () => {
            temp = init;
            return temp;
        },
    }
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */