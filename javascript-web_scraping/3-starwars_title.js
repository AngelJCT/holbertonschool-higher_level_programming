#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }
    console.log(JSON.parse(body).title);
});
