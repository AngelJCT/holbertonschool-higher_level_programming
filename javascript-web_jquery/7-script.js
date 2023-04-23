#!/usr/bin/node
// script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  type: 'GET',
  dataType: 'json',
  success: function (data) {
    $('DIV#character').text(data.name);
  }
});
