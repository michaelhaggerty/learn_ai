
let name = "Mike";
console.log(name);

//Variables

// 1. Cannot be a reserved keyword (typeof, )
// 2. should be meaningful/indicative
// 3. cannot start with a number (1name)
// 4. cannot contain spaces or hyphens
// 5. are case sensitive (just stick to camelNotation)

// we can change the value of variables
let interestRate = 0.01;
interestRate = 0.02;
console.log(interestRate);

//sometimes we want to keep constant, so use "constants"
const fixedInterestRate = 0.01;
//fixedInterestRate = 1; //this will throw an error
console.log(fixedInterestRate);

//what kind of values can we assign to variables? 

let firstName = "Mike"; //String Literal
let age = 30; //Number Literal (no floating point/integer)
let isApproved = true; //Boolean Literal
let middleName = undefined; //Undefined Literal (not common)
let lastName = null; //Null - use where we want to clear the value of variable

// Dynamic Typing - Statis vs Dynamic(variable type can change at runtime)
typeof name //

// undefined is a type and a value
// null is an object

let selectedColor = null; //typeof is object

// Reference Types - objects, arrays, functions

//object - like an object in real life

let person ={
    name: "Mike",
    age: 29
}
console.log(person);

// we can interact with two types of notation

// dot 
console.log(person.name);

// bracket - if we don't know what property we need yet
console.log(person['name'])
//usage
let selection = 'name';
person[selection] = 'Mark';
console.log(person.name);

//Arrays
let selectedColors = ["red", "blue", "green", "black"];
console.log(selectedColors.length);