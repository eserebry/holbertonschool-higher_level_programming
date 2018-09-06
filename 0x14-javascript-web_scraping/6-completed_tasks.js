#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let userIdList = JSON.parse(body);
    let dict = {};
    for (let i = 0; i < userIdList.length; i++) {
      if (userIdList[i].completed === true) {
        if (dict[userIdList[i].userId] === undefined) {
          dict[userIdList[i].userId] = 1;
        } else { dict[userIdList[i].userId]++; }
      }
    }
    console.log(dict);
  }
}
);
