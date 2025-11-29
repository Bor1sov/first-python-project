class Person{
    isHuman = true;
    constructor(name,surname,age){
        this.name = name;
        this.surname = surname;
        this.age = age;
    }
    getName(){
        return `My name is ${this.name}`
    }
    getSurname(){
        return `My surname is ${this.surname}`
    }
    getAge(){
        return `My age is ${this.age}`
    }
}

const egor = new Person('Egor','Borisov',21)

console.log(egor.getAge())