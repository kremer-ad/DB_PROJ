import * as fs from 'fs';
import {Garage} from "./Garage" 


fs.readFile('./garages.csv','utf8',(error,data)=>{
    let lines = data.toString().split('\n').slice(1)
    let results:string[] = []
    for(let i =0;i<lines.length;i++){
        let splittedLine = lines[i].split('|')
        // console.log(line)
        if(splittedLine == undefined ||splittedLine.length< 10){
            continue
        }
        let garage:Garage = new Garage(splittedLine[4].slice(1,-1).concat(' , ',splittedLine[5].slice(1,-1)),splittedLine[1],splittedLine[6])
        if(results.indexOf(garage.toString())==-1){
            results.push(garage.toString())
        }
    }
    let resultsStr = ""
    for(let i=0;i<results.length;i++){
        resultsStr = resultsStr.concat(i.toString(),'\t',results[i],'\n')

    }
    fs.writeFileSync('./resultsGarages.csv',resultsStr)
});
