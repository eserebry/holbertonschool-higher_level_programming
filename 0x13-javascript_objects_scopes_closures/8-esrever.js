#!/usr/bin/node
exports.esrever = function (list) {
  let reverse = [];
  for (let j = list.length - 1; j >= 0; j--) {
    reverse.push(list[j]);
  }
  return (reverse);
};
