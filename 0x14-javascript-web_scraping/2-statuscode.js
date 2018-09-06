#!/usr/bin/node
const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options)
  .on('response', function (response) {
    console.log('code: ' + response.statusCode);
  });
