#!/usr/bin/node
// prints "C is fun" x times
// where x is the first argument of the script
// if no argument is passed, print "Missing number of occurrences"
// You must use console.log(...) to print all output
// You are not allowed to use var

const args = process.argv.slice(2);
const x = parseInt(args[0]);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
