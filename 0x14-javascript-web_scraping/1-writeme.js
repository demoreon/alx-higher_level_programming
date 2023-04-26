#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const s_text = process.argv[3];

fs.writeFile(file, s_text, 'utf-8', function (err) {
  if (err) console.log(err);
});
