#!/usr/bin/node
const request = require('request');
const movieUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(movieUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movieInfo = JSON.parse(body);
    console.log(movieInfo.title);
  }
});
