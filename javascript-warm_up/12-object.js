#!/usr/bin/node

function findSecondLargest (numList) {
  let largest = numList[0];
  let secondLargest = -Infinity;
  for (let i = 1; i < numList.length; i++) {
    if (numList[i] > largest) {
      secondLargest = largest;
      largest = numList[i];
    } else if (numList[i] < largest && numList[i] > secondLargest) {
      secondLargest = numList[i];
    }
  }
  return secondLargest;
}

const args = process.argv.slice(2);
const argNums = args.map(Number);
console.log(findSecondLargest(argNums));
