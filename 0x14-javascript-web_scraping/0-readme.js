#!/usr/bin/node

// Import the process.argv and fs module
const { argv } = require('node:process');
const fs = require('node:fs');

// Read and priint file content or print error message
fs.readFile(argv[2], 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});
