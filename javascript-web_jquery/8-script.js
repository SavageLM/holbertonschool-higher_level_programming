#!/usr/bin/node
$.get('https://swapi-api.hbtn.io/api/films/?format=json', (movieData) => {
  $('UL#list_movies').append(movieData.results.map((movie) => `<li>${movie.title}</li>`));
});
