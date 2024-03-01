/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    count = 0;
    for (let i = 0; i < operations.length; i++){
        if (operations[i][0] == '-' || operations[i][2] == '-') count--;
        else count += 1;
    }
    return count;
};