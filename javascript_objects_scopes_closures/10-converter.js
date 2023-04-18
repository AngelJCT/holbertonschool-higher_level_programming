#!/usr/bin/node
// function to convert a number from base 10 to another base passed as argument
exports.converter = function (base) {
  return function (num) { // returns another function which takes 'num' as argument
    return num.toString(base); // inner function that uses 'toString' method to convert the number to a string representation in the specified base
  };
};

/*
The reason for converting the number to a string representation in the specified base is mainly for readability and ease of use.
When converting a number to another base, the output can include characters other than digits (0-9).
For example, in base 16 (hexadecimal), you have the characters A-F in addition to the digits 0-9. Representing the output as a string makes
it easier to work with and display the result.

When you convert a number to a different base, it's typically for human consumption, such as displaying it on a webpage or in a log file.
By returning a string, you can easily print, concatenate, or otherwise manipulate the result as needed. If the output were a number instead, it
would require additional parsing and processing to display or manipulate the result correctly.

In summary, converting the number to a string representation in the specified base provides a convenient and human-readable format for working
with and displaying the result.
*/