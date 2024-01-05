#!/usr/bin/node

// Import process and request module
const process = require('process');
const request = require('request');

const requestURL = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];

request(`${requestURL}${id}`, function (error, response, body) {
  const bodyResponse = JSON.parse(body).title;

  if (error) {
    console.error('error:', error);
  }

  console.log(bodyResponse);
});
