#!/usr/bin/node
let list = require('./100-data.js').list;
const map1 = list.map((x, i) => x * i);
console.log(map1);
console.dir(list);
