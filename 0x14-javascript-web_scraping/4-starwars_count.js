#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const obj = JSON.parse(body);
  let total = 0;

  for (const result of obj.results) {
    for (const character of result.characters) {
      if (character.includes('18')) total += 1;
    }
  }
  console.log(total);
});
