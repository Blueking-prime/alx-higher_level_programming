#!/usr/bin/node
function add (a, b) {
  const result = parseInt(a, 10) + parseInt(b, 10);
  console.log(result);
}
add(process.argv[2], process.argv[3]);
