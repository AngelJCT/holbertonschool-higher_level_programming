#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const characterId = '18';
const characterUrl = 'https://swapi-api.hbtn.io/api/people/' + characterId;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (const film of films) {
    if (film.characters.includes(characterUrl)) {
      count++;
    }
  }
  console.log(count);
});
