#!/usr/bin/node

function findSecondBiggest (numList) {
  let biggest = numList[0];
  let secondBiggest = -Infinity;
  for (let i = 1; i < numList.length; i++) {
    if (numList[i] > biggest) {
      secondBiggest = biggest;
      biggest = numList[i];
    } else if (numList[i] < biggest && numList[i] > secondBiggest) {
      secondBiggest = numList[i];
    }
  }
  return secondBiggest;
}

const args = process.argv.slice(2);
const argNums = args.map(Number);
if (argNums.length < 2) {
  console.log(0);
} else {
  console.log(findSecondBiggest(argNums));
}
