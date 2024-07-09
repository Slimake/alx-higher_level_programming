#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);

if (isNaN(firstArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArg; i++) {
    const arrOfX = [];
    let str = '';

    for (let j = 0; j < firstArg; j++) {
      arrOfX[j] = 'X';
    }

    str = arrOfX.join('');
    console.log(str);
  }
}
