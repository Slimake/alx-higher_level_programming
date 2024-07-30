#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode === 200) {
    const results = JSON.parse(body).results;
    let total = 0;

    for (const result of results) {
      for (const character of result.characters) {
        if (character.includes('18')) total += 1;
      }
    }

    console.log(total);
  } else {
    console.log('Error Code:', response.statusCode);
  }
});
