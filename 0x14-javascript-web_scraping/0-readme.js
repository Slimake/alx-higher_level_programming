#!/usr/bin/node

// Import the process.argv and fs module
const process = require('process');
const fs = require('fs');

const filepath = process.argv[2];

// Read and priint file content or print error message
fs.readFile(filepath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
