#!/usr/bin/node
// script that fetches and lists all movies title by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  type: 'GET',
  dataType: 'json',
  success: function (data) {
    for (let i = 0; i < data.results.length; i++) {
      $('UL#list_movies').append('<li>' + data.results[i].title + '</li>');
    }
  }
});
