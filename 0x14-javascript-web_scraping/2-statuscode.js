#!/usr/bin/node

// Import the request module
const process = require('process');
const request = require('request');

const requestURL = process.argv[2];

request.get(requestURL, function (error, response) {
  if (error) {
    console.error('error:', error);
  }
  console.log('code:', response.statusCode);
});
