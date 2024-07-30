#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const baseURL = 'https://swapi-api.alx-tools.com/api/';
const filmsURL = `${baseURL}films`;
const episodeURL = `${filmsURL}/${movieID}`;

request(episodeURL, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const obj = JSON.parse(body);

  console.log(obj.title);
});
