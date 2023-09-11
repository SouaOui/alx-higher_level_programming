#!/usr/bin/node
const args = process.argv;
let i = 0;
if (typeof args[2] === 'undefined') {
  console.log('Missing number of occurrences');
}
if (Math.sign(args[2]) === -1) {
  process.exit(0);
}
if (typeof args[2] !== 'undefined') {
  while (i < args[2]) {
    console.log('C is fun');
    i++;
  }
}
