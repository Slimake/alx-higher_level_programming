#!/usr/bin/node

// Import fs and process module
const fs = require('fs');
const process = require('process');

const filename = process.argv[2];
const content = process.argv[3];

fs.writeFile(filename, content, (err) => {
  if (err) {
    console.error(err);
  }
});
