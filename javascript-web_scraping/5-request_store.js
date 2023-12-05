#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const wantedUrl = process.argv[2];
const filePath = process.argv[3];
request(wantedUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  fs.writeFile(filePath, body, (error) => {
    if (error) {
      console.log(error);
    }
  });
});
