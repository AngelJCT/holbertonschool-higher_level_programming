#!/usr/bin/node
// script that updates the text color of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header:
$('DIV#red_header').click(function () {
    $('header').css('color', '#FF0000');
    }
);
