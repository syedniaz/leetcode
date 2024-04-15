/**
 * @param {number[]} nums
 * @param {number[]} index
 * @return {number[]}
 */
var createTargetArray = function(nums, index) {
    ta = [];
    for (let i = 0; i < nums.length; i++){
        ta.splice(index[i], 0, nums[i]);
    }
    return ta;
};