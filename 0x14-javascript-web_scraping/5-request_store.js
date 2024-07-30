#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  // If there is an error
  if (error) throw error;

  if (response.statusCode === 200) {
    // Write to file
    fs.writeFile(filePath, body, error => {
      if (error) throw error;
    });
  }
});
