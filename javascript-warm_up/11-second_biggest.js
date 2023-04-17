#!/usr/bin/node
// prints the second biggest integer in the list of arguments
// If no argument passed, print 0
// If the number of arguments is 1, print 0
// You must use console.log(...) to print all output
// You are not allowed to use var

const args = process.argv.slice(2);
const num = args.map(arg => parseInt(arg));
function secondBiggest (num) {
  if (num.length === 0) {
    return 0;
  } else if (num.length === 1) {
    return 0;
  } else {
    num.sort((a, b) => a - b); // sort the integers in ascending order
    return num[num.length - 2]; // return the second largest integer
  }
}
console.log(secondBiggest(num));
