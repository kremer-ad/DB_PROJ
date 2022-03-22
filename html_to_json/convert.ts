import fs = require('fs')

fs.readFile('.\\models_html_element.txt',(error,data)=>{
    let rows:string[] = data.toString().split('<tr>')
    let results =""
    for(let row of rows.slice(1)){
        let parts:string[] = row.split('<td')
        let model:string = parts[2]
        model = model.slice(model.indexOf('0">')+3,model.indexOf('</div>'))
        let make:string = parts[3]
        make = make.slice(make.indexOf('0">')+3,make.indexOf('</div>'))
        //let year:string = parts[4]
        let yearsTags:string[] = parts[4].split('<span>')
        let years:string[] = []

        for(let year of yearsTags.slice(1)){
            years.push(year.slice(year.indexOf(';">')+3,year.indexOf('</a>')))
        }
        console.log(years)
        for(let year of years){
            results = results.concat(model,',',make,',',year,'\n')
        }
    }
    fs.writeFile('results.csv',results,callback=>{})
}); 