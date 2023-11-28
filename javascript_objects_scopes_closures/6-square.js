#!/usr/bin/node

const SquareOne = require('./5-square');

class Square extends SquareOne {
  charprint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        let row = '';
        for (let j = 0; j < this.size; j++) {
          row += 'c';
        }
        console.log(row);
      }
    }
  }
}
module.exports = Square;
