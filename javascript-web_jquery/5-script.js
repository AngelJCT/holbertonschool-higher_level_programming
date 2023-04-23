#!/usr/bin/node
// script that adds a LI element to a list when the user clicks on the tag DIV#add_item
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
