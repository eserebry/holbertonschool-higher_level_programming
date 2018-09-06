#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const id = 18;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let results = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      let chrct = results[i].characters;
      for (let j = 0; j < chrct.length; j++) {
        if (chrct[j].indexOf(id) >= 0) { count++; }
      }
    }
    console.log(count);
  }
});
