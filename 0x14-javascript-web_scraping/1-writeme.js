#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
  console.log('Usage: node write_file.js <file_path> <data-to-write>');
  process.exit(1);
}

const filePath = process.argv[2];
const dataToWrite = process.argv[3];

fs.writeFile(filePath, dataToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
