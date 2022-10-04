#!/usr/bin/node
function factorial (n) {
  if (n === 0) {
    return 1;
  }
  if (isNaN(n)) {
    return 1;
  }

  return (n * factorial(n - 1));
}
const value = factorial(parseInt(process.argv[2]));
console.log(value);
