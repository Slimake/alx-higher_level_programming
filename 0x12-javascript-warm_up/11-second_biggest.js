#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arrOfNum = process.argv.slice(2);
  const sortedArr = arrOfNum.sort((a, b) => a - b);
  const secondMax = sortedArr[sortedArr.length - 2];

  console.log(secondMax);
}
