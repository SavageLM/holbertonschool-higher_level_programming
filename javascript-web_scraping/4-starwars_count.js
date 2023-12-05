#!/usr/bin/node
const request = require('request');
const movieUrl = process.argv[2];
request(movieUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movieInfo = JSON.parse(body);
    let count = 0;
    for (let i = 0; i < movieInfo.length; i++) {
      if (movieInfo.character.endswith('/18/')) {
        count++;
      }
    }
    console.log(count);
  }
});
