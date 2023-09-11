#!/usr/bin/node
const args = process.argv;
const length = args.length;
let i = 0;
if (typeof args[2] === 'undefined') {
  console.log('Missing number of occurrences');
}
if (Math.sign(args[2]) === -1) {
  process.exit(0);
}
if (typeof args[2] !== 'undefined') {
  while (i < length) {
    console.log('C is fun');
    i++;
  }
}
