/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address) {
    newAdd = address.replaceAll(".", "[.]");
    return newAdd;
};