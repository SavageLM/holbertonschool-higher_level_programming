#!/usr/bin/node

const size = parseInt(process.argv[2]);
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let i = 0; i < size; i++) {
      row += 'X';
    }
    console.log(row);
  }
}
