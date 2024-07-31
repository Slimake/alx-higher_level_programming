#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

let filmCharacters = [];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const film = JSON.parse(body);
    filmCharacters = film.characters;
  }

  for (const charURL of filmCharacters) {
    request(charURL, (error, response, body) => {
      if (error) {
        console.log(error);
      } else {
        const character = JSON.parse(body);
        console.log(character.name);
      }
    });
  }
});
