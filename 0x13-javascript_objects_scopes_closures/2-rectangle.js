#!/usr/bin/node
module.exports = class Rectangle {
  constructor (width, height) {
    if (width <= 0 || height <= 0 || !width || !height) {
      module.exports = class Rectangle {};
    } else {
      this.width = width;
      this.height = height;
    }
  }
};
