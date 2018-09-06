#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/';
const id = process.argv[2];

request(url + id, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let chrct = JSON.parse(body).characters;
    for (let i = 0; i < chrct.length; i++) {
      request(chrct[i], function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
