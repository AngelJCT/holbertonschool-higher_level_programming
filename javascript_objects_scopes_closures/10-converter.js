#!/usr/bin/node
// function to convert a number from base 10 to another base passed as argument
exports.converter = function (base) {
  return function (num) { // returns another function which takes 'num' as argument
    return num.toString(base); // inner function that uses 'toString' method to convert the number to a string representation in the specified base
  };
};
