#!/usr/bin/node

const req = require('request');
const i_d = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/';
req.get(URL + i_d, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const info = JSON.parse(body);
  const dd = info.characters;
  for (const i of dd) {
    req.get(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const info1 = JSON.parse(body1);
      console.log(info1.name);
    });
  }
});
