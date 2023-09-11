#!/usr/bin/node
const process = require('process');
const args = process.argv;
const message = 'My Number: ';
if (!isNaN(parseInt(args[2], 10))){
  console.log(message + parseInt(args[2], 10));
} else {
  console.log('Not a number');
}
