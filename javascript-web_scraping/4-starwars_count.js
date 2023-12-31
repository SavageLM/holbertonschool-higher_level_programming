#!/usr/bin/node
const request = require('request');
const movieUrl = process.argv[2];
request(movieUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movieInfo = JSON.parse(body);
    let count = 0;
    movieInfo.results.forEach((movie) => {
      if (movie.characters.forEach((character) => character.endsWith('/18/'))) {
        count += 1;
      }
    });
    console.log(count);
  }
});
