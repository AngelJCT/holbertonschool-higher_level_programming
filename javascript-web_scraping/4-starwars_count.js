#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
}
);
