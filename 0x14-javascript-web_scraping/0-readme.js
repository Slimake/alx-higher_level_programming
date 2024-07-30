#!/usr/bin/node

const fs = require('node:fs');
const filename = process.argv[2];

fs.readFile(filename, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
