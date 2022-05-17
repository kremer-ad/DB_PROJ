"use strict";
var __values = (this && this.__values) || function(o) {
    var s = typeof Symbol === "function" && Symbol.iterator, m = s && o[s], i = 0;
    if (m) return m.call(o);
    if (o && typeof o.length === "number") return {
        next: function () {
            if (o && i >= o.length) o = void 0;
            return { value: o && o[i++], done: !o };
        }
    };
    throw new TypeError(s ? "Object is not iterable." : "Symbol.iterator is not defined.");
};
var __read = (this && this.__read) || function (o, n) {
    var m = typeof Symbol === "function" && o[Symbol.iterator];
    if (!m) return o;
    var i = m.call(o), r, ar = [], e;
    try {
        while ((n === void 0 || n-- > 0) && !(r = i.next()).done) ar.push(r.value);
    }
    catch (error) { e = { error: error }; }
    finally {
        try {
            if (r && !r.done && (m = i["return"])) m.call(i);
        }
        finally { if (e) throw e.error; }
    }
    return ar;
};
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
exports.__esModule = true;
var fs = require("fs");
fs.readFile('.\\models_html_element.txt', function (error, data) {
    var e_1, _a, e_2, _b, e_3, _c;
    var rows = data.toString().split('<tr>');
    var resultsModel = "";
    var resultsMake = "";
    var makes = [];
    var modelId = 0;
    try {
        for (var _d = __values(rows.slice(1)), _e = _d.next(); !_e.done; _e = _d.next()) {
            var row = _e.value;
            var parts = row.split('<td');
            var model = parts[2];
            model = model.slice(model.indexOf('0">') + 3, model.indexOf('</div>'));
            var make = parts[3];
            make = make.slice(make.indexOf('0">') + 3, make.indexOf('</div>'));
            //let year:string = parts[4]
            var yearsTags = parts[4].split('<span>');
            var years = [];
            if (!(make in makes)) {
                makes.push(make);
            }
            try {
                for (var _f = (e_2 = void 0, __values(yearsTags.slice(1))), _g = _f.next(); !_g.done; _g = _f.next()) {
                    var year = _g.value;
                    years.push(year.slice(year.indexOf(';">') + 3, year.indexOf('</a>')));
                }
            }
            catch (e_2_1) { e_2 = { error: e_2_1 }; }
            finally {
                try {
                    if (_g && !_g.done && (_b = _f["return"])) _b.call(_f);
                }
                finally { if (e_2) throw e_2.error; }
            }
            try {
                for (var years_1 = (e_3 = void 0, __values(years)), years_1_1 = years_1.next(); !years_1_1.done; years_1_1 = years_1.next()) {
                    var year = years_1_1.value;
                    resultsModel = resultsModel.concat((modelId++).toString(), ',', model, ',', makes.indexOf(make).toString(), ',', year, '\n');
                }
            }
            catch (e_3_1) { e_3 = { error: e_3_1 }; }
            finally {
                try {
                    if (years_1_1 && !years_1_1.done && (_c = years_1["return"])) _c.call(years_1);
                }
                finally { if (e_3) throw e_3.error; }
            }
        }
    }
    catch (e_1_1) { e_1 = { error: e_1_1 }; }
    finally {
        try {
            if (_e && !_e.done && (_a = _d["return"])) _a.call(_d);
        }
        finally { if (e_1) throw e_1.error; }
    }
    fs.writeFile('resultsModel.csv', resultsModel, function (callback) { });
    makes = __spreadArray([], __read(new Set(makes)), false);
    for (var i = 0; i < makes.length; i++) {
        resultsMake = resultsMake.concat(i.toString(), ',', makes[i], '\n');
    }
    fs.writeFile('resultsMake.csv', resultsMake, function (c) { });
});
