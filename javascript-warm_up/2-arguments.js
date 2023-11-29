#!/usr/bin/node

const argNum = process.argv.length - 2;
if (argNum === 0) {
  console.log('No Argument');
} else if (argNum === 1) {
  console.log('Arguement found');
} else {
  console.log('Arguements found');
}
