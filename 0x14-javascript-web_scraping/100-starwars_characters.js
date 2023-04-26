#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/';
request.get(URL + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const i of dd) {
    request.get(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const info1 = JSON.parse(body1);
      console.log(info1.name);
    });
  }
});
