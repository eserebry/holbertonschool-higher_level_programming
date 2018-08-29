#!/usr/bin/node
function factorial (n) {
  if (n === 0 || isNaN(n) === true) {
    return 1;
  } else {
    return (factorial(n - 1) * n);
  }
}
console.log(factorial(parseInt(process.argv[2])));
