#!/usr/bin/node
// script that fetches from https://stefanbohacek.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello
$.ajax({
  url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
  type: 'GET',
  dataType: 'json',
  success: function (data) {
    $('DIV#hello').text(data.hello);
  }
});
