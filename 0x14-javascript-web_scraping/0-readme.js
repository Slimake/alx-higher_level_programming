#!/usr/bin/node

const fs = require('node:fs');
const filename = process.argv[2];
const filePath = `./${filename}`;

fs.readFile(`${filePath}`, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
