#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];
fs.writeFile(filePath, content, (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
