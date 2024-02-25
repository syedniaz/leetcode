var buildArray = function(nums) {
    let numss = [];
    nums.forEach (function (num,i){
        numss[i] = nums[num];
    })
    return numss;
};