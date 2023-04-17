#!/usr/bin/node
// computes and print a factorial
// The first argument is integer (argument can be cast as integer) used for computing the factorial
// Factorial of NaN is 1
// You must do it recursively
// You must use a function
// You must use console.log(...) to print all output
// You are not allowed to use var

const args = process.argv.slice(2);
const num = parseInt(args[0]);
function factorial (num) {
  if (isNaN(num)) {
    return 1;
  }
  if (num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(num));
