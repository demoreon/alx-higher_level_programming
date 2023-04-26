#!/usr/bin/node

const request = require('request');
const link_url = process.argv[2];

request(link_url, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
