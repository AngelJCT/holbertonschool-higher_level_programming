#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }
  
  charPrint (c) {
    if (c === undefined) {
        this.print();
    } else {
        let output = '';
        for (let i = 0; i < this.height; i++) {
          for (let j = 0; j < this.width; j++) {
            output += c;
          }
          if (i < this.height - 1) {
            output += '\n';
          }
        }
        console.log(output);
    }
  }
}
module.exports = Square;
