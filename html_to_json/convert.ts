import * as fs from 'fs'

fs.readFile('.\\models_html_element.txt',(error,data)=>{
    let rows:string[] = data.toString().split('<tr>')
    let resultsModel:string =""
    let resultsMake:string = ""
    let makes:string[] = []
    let modelId = 0
    for(let row of rows.slice(1)){
        let parts:string[] = row.split('<td')
        let model:string = parts[2]
        model = model.slice(model.indexOf('0">')+3,model.indexOf('</div>'))
        let make:string = parts[3]
        make = make.slice(make.indexOf('0">')+3,make.indexOf('</div>'))
        //let year:string = parts[4]
        let yearsTags:string[] = parts[4].split('<span>')
        let years:string[] = []
        if(!(make in makes)){
            makes.push(make)
        }
        makes = [...new Set(makes)]
        for(let year of yearsTags.slice(1)){
            years.push(year.slice(year.indexOf(';">')+3,year.indexOf('</a>')))
        }

        for(let year of years){
            resultsModel = resultsModel.concat((modelId++).toString(),',',model,',',makes.indexOf(make).toString(),',',year,'\n')
        }
    }
    fs.writeFile('resultsModel.csv',resultsModel,callback=>{})

    for(let i=0;i<makes.length;i++){
        resultsMake = resultsMake.concat(i.toString(),',',makes[i],'\n')
    }
    fs.writeFile('resultsMake.csv',resultsMake,c=>{})
}); 