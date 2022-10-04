#!/usr/bin/node
const len = process.argv.length;
if (len <= 3) {
  console.log(0);
} else {
  const newList = process.argv.slice(2);
  newList.sort(function (a, b) { return a - b; });
  console.log(newList[len - 4]);
}
