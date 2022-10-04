#!/usr/bin/node
const x = parseInt(process.argv[2], 10);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let squareText = '';
    for (let j = 0; j < x; j++) {
      squareText += 'X';
    }
    console.log(squareText);
  }
}
