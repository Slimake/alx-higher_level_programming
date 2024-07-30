#!/usr/bin/node

const request = require('request');

// Request URL
const url = process.argv[2];

request(url, (error, response, body) => {
  // Print the error if occurred
  if (error) console.error(error);
  console.log('code:', response.statusCode);
});
