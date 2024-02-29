/**
 * @param {number} big
 * @param {number} medium
 * @param {number} small
 */
var ParkingSystem = function(big, medium, small) {
    this.bigSlot = big;
    this.medSlot = medium;
    this.smallSlot = small;
};

/** 
 * @param {number} carType
 * @return {boolean}
 */
ParkingSystem.prototype.addCar = function(carType) {
    if (carType == 1){
        if (this.bigSlot > 0) {
            this.bigSlot--;
            return true;
        }
        else return false;
    }
    else if (carType == 2){
        if (this.medSlot > 0) {
            this.medSlot--;
            return true;
        }
        else return false;
    }
    else if (carType == 3){
        if (this.smallSlot > 0) {
            this.smallSlot--;
            return true;
        }
        else return false;
    }
};

/** 
 * Your ParkingSystem object will be instantiated and called as such:
 * var obj = new ParkingSystem(big, medium, small)
 * var param_1 = obj.addCar(carType)
 */