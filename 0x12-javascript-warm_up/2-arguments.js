#!/usr/bin/node

const { argv } = require('node:process');

// Checks if command-line arguments found or not.
if (argv.length === 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else if (argv.length > 3) {
  console.log('Arguments found');
}
