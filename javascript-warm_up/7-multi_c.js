#!/usr/bin/node

const repeats = parseInt(process.argv[2]);
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < repeats; i++) {
    console.log('C is fun');
  }
}
