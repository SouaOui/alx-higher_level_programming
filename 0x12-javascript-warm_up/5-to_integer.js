#!/usr/bin/node
const { argv } = require('process');
const message = 'My Number: ';
if (!isNaN(parseInt(argv[2], 10))) {
  console.log(message + parseInt(argv[2], 10));
} else {
  console.log('Not a number');
}
