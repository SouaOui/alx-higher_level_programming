#!/usr/bin/node
const process = require('process');
const args = process.argv;
const numberInt = parseInt(args[2], 10);
if (!isNaN(numberInt)) {
  console.log(numberInt);
} else {
  console.log('Not a number');
}
