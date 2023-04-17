#!/usr/local/bin/node

const args = process.argv.slice(2);

if (!isNaN(args) && Number.isInteger(parseFloat(args))) {
  console.log('My number: ' + parseInt(args[0]));
} else {
  console.log('Not a number');
}
