"use strict";
exports.__esModule = true;
var fs = require("fs");
var Garage_1 = require("./Garage");
fs.readFile('./garages.csv', 'utf8', function (error, data) {
    var lines = data.toString().split('\n').slice(1);
    var results = [];
    for (var i = 0; i < lines.length; i++) {
        var splittedLine = lines[i].split('|');
        // console.log(line)
        if (splittedLine == undefined || splittedLine.length < 10) {
            continue;
        }
        var garage = new Garage_1.Garage(splittedLine[4].slice(1, -1).concat(' , ', splittedLine[5].slice(1, -1)), splittedLine[1], splittedLine[6]);
        if (results.indexOf(garage.toString()) == -1) {
            results.push(garage.toString());
        }
    }
    var resultsStr = "";
    for (var i = 0; i < results.length; i++) {
        resultsStr = resultsStr.concat(i.toString(), '\t', results[i], '\n');
    }
    fs.writeFileSync('./resultsGarages.csv', resultsStr);
});
