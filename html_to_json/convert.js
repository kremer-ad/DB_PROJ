"use strict";
exports.__esModule = true;
var fs = require("fs");
fs.readFile('.\\models_html_element.txt', function (error, data) {
    var rows = data.toString().split('<tr>');
    var results = "";
    for (var _i = 0, _a = rows.slice(1); _i < _a.length; _i++) {
        var row = _a[_i];
        var parts = row.split('<td');
        var model = parts[2];
        model = model.slice(model.indexOf('0">') + 3, model.indexOf('</div>'));
        var make = parts[3];
        make = make.slice(make.indexOf('0">') + 3, make.indexOf('</div>'));
        //let year:string = parts[4]
        var yearsTags = parts[4].split('<span>');
        var years = [];
        for (var _b = 0, _c = yearsTags.slice(1); _b < _c.length; _b++) {
            var year = _c[_b];
            years.push(year.slice(year.indexOf(';">') + 3, year.indexOf('</a>')));
        }
        console.log(years);
        for (var _d = 0, years_1 = years; _d < years_1.length; _d++) {
            var year = years_1[_d];
            results = results.concat(model, ',', make, ',', year, '\n');
        }
    }
    fs.writeFile('results.csv', results, function (callback) { });
});
