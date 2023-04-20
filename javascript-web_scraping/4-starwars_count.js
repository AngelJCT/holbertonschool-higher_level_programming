#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const characterId = '18';

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).results; // parse the JSON response to get the list of films
  let count = 0;
  films.forEach(film => { // iterate through each film in the films array
    film.characters.forEach(character => { // for each film, iterate through the characters in the film
      if (character.includes(characterId)) { // if the character match the id, add to count
        count++;
      }
    });
  });
  console.log(count);
});
