#!/usr/bin/node
let list = require('./100-data.js').list;
const map1 = list.map((x, i) => x * i);
console.dir(list);
console.log(map1);
