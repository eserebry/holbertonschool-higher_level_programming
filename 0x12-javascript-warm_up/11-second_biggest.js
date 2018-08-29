#!/usr/bin/node
let size = process.argv.length;
let a, max, second;
if (size <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < size; i++) {
    a = parseInt(process.argv[i], 10);
    if (i === 2) {
      max = a;
    }
    if (a > max) {
      second = max;
      max = a;
    } else {
      second = a;
    }
  }
  console.log(second);
}
