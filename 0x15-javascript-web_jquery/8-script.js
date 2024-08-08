const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$(document).ready(function () {
  $.get(url, function (data, textStatus) {
    if (textStatus === 'success') {
      for (const film of data.results) {
        $('UL#list_movies').append('<li>' + film.title + '</li>');
      }
    }
  });
});
