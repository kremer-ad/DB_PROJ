export class Garage {
    location:string
    name:string
    phoneNumber:string

    constructor(location:string,name:string,phoneNumber:string){
        this.name = name
        this.location = location
        this.phoneNumber = phoneNumber
    }

    public toString():string {
        return "".concat(this.location,'\t',this.name.slice(1,-1),'\t',this.phoneNumber.slice(1,-1))
    }


}
