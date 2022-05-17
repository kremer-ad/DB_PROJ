"use strict";
exports.__esModule = true;
exports.Garage = void 0;
var Garage = /** @class */ (function () {
    function Garage(location, name, phoneNumber) {
        this.name = name;
        this.location = location;
        this.phoneNumber = phoneNumber;
    }
    Garage.prototype.toString = function () {
        return "".concat(this.location, '\t', this.name.slice(1, -1), '\t', this.phoneNumber.slice(1, -1));
    };
    return Garage;
}());
exports.Garage = Garage;
