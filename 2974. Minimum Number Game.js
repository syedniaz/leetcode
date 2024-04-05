/**
 * @param {number[]} nums
 * @return {number[]}
 */
var numberGame = function(nums) {
    let swapped = false;
    for (let i = 0; i<nums.length - 1; i++){
        swapped = false;
        for (let j = 0; j<nums.length - 1; j++){
            if (nums[j] > nums[j + 1]) {
                temp = nums[j];
                nums[j] = nums[j + 1];
                nums[j + 1] = temp;
                swapped = true;
            }
        }
        if (swapped == false)
            break;
    }
    //bubble sort
    
    for (let i = 0; i<nums.length; i = i+2){
        temp1 = nums[i];
        temp2 = nums [i+1];
        nums[i] = temp2;
        nums [i+1] = temp1;
    }
    return nums;
};