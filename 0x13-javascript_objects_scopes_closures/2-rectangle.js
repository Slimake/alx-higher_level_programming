#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;

    if ((w < 1 || w === undefined) || (h < 1 || h === undefined)) {
      delete this.width;
      delete this.height;
    }
  }
};
