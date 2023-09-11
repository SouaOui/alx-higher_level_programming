#!/usr/bin/node
const { argv } = require('process');
const IntNumber = parseInt(argv[2], 10);
if (argv[2] === 'undefined' || isNaN(parseInt(argv[2], 10))) {
  console.log('Missing size');
}
if (Math.sign(argv[2]) === -1) {
  process.exit(0);
}
if (typeof argv[2] !== 'undefined') {
  for (let i = 0; !isNaN(argv[2]) && i < IntNumber; i++) {
    console.log('X'.repeat(IntNumber));
  }
}
