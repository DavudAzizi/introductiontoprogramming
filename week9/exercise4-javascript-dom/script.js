console.log("JavaScript loaded!");

let username = prompt("What is your name?");

if (username)
{
    alert("Welcome, " + username + "!");
}

let number1 = Number(prompt("Enter first number:"));
let number2 = Number(prompt("Enter second number:"));

let sum = number1 + number2;

console.log("Sum:", sum);

function greet(name)
{
    return "Hello, " + name;
}

console.log(greet(username));

for (let i = 1; i <= 5; i++)
{
    console.log("Count:", i);
}
