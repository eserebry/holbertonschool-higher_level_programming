#!/usr/bin/node
let x = 'X';
let size = parseInt(process.argv[2], 10);
if (isNaN(size) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log(x.repeat(size));
  }
}
