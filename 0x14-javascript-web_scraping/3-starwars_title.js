#!/usr/bin/node

// Import process and request module
const process = require('process');
const request = require('request');

const id = process.argv[2];
const requestURL = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(requestURL, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else if (response.statusCode === 200) {
    body = JSON.parse(body);
    console.log(body.title);
  } else {
    console.log('statusCode:', response.statusCode);
  }
});
