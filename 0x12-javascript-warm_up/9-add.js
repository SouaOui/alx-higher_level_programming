#!/usr/bin/node
const args = process.argv;
const a = parseInt(args[2], 10);
const b = parseInt(args[3], 10);
function add (a, b) {
  return a + b;
}
console.log(add(a, b));
