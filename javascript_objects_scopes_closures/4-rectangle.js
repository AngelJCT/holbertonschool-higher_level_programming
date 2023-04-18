#!/usr/bin/node
// Class Rectangle that defines a rectangle
// If w or h is equal to 0 or not a positive integer, create an empty object
// Create an instance method called print() that prints the rectangle using the character X
// You must use the character X to print the rectangle
// The width and height of the rectangle are based on the integer passed as parameters

class Rectangle {
    constructor (w, h) {
      if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
        return;
      }
      this.width = w;
      this.height = h;
    }
  
    print () {
      let output = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          output += 'X';
        }
        if (i < this.height - 1) {
          output += '\n';
        }
      }
      console.log(output);
    }

    rotate () {
      let temp = this.width;
      this.width = this.height;
      this.height = temp;
    }

    double () {
      this.width *= 2;
      this.height *= 2;
    }
  }
  module.exports = Rectangle;
