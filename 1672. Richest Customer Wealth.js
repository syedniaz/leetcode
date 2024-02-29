/**
 * @param {number[][]} accounts
 * @return {number}
 */
let maximumWealth = function(accounts) {
    var sum = 0, temp = 0;
    for (let i = 0; i < accounts.length; i++){
        temp = 0;
        for (let j = 0; j < accounts[i].length; j++){
            temp += accounts[i][j];
        }
        if (temp > sum) sum = temp;
    }
    return sum;
};