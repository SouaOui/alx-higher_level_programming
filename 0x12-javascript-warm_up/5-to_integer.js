#!/usr/bin/node
const process = require('process');
const args = process.argv;
const message = 'My Number: ';
const numberInt = parseInt(args[2], 10);
if (!isNaN(numberInt)) {
  console.log(message + numberInt);
} else {
  console.log('Not a number');
}
