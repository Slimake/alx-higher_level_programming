#!/usr/bin/node

const fs = require('node:fs');
const filename = process.argv[2];
const content = process.argv[3];

fs.writeFile(filename, content, err => {
  if (err) throw err;
});
