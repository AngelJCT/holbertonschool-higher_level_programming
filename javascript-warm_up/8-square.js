#!/usr/bin/node
// prints a square
// The first argument is the size of the square
// If the first argument can’t be converted to an integer, print “Missing size”
// You must use the character X to print the square
// You must use console.log(...) to print all output
// You are not allowed to use var
// You are not allowed to use any if/else statement
// You must use a loop (while, for, etc.)

const args = process.argv.slice(2);
const x = parseInt(args[0]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
