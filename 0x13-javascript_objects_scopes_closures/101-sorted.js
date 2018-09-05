#!/usr/bin/node
let dict = require('./101-data.js').dict;
console.log(dict);
let value = [];
for (let key in dict) {
    value.push(dict[key]);;
}
console.log(value);
