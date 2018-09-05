#!/usr/bin/node
const fs = require('fs');
let text = fs.readFileSync('./cisfun', 'utf-8');
console.log(text);
