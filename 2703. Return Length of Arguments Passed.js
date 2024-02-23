var argumentsLength = function(...args) {
    let count = 0;
    args.forEach(() => {count++;});
    return count;
};