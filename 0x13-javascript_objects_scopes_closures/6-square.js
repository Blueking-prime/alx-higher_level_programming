#!/usr/bin/node

const squareModel = require('./5-square');

module.exports = class Square extends squareModel {
  constructor (size) {
    super(size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += c;
      }
      console.log(line);
    }
  }
};
