#!/usr/bin/node

const args = process.argv.slice(2);

if (args[0]) {
  console.log(args[0] + ' is ' + args[1]);
} else {
  console.log(undefined + ' is ' + undefined);
}