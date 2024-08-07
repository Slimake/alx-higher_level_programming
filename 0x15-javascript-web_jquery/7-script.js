const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$(document).ready(function () {
  $.get(url, function (data, textStatus) {
    if (textStatus === 'success') {
      $('DIV#character').text(data.name);
    }
  });
});
