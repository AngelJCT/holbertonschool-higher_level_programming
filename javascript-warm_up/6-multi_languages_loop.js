#!/usr/bin/node
// prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

function multiLanguages2 () {
  const array = ['C is fun', 'Python is cool', 'Javascript is amazing'];
  for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
  }
}

multiLanguages2();
