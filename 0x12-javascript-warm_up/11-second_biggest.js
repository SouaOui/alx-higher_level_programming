#!/usr/bin/node
const args = process.argv;
const length = args.length;
let max = parseInt(args[2]);
for (let i = 0; i < length; i++) {
  if (parseInt(args[i]) > max) {
    max = parseInt(args[i]);
  }
}
console.log(max);
