#!/usr/bin/node
const args = process.argv;
const length = args.length;
if (length === 2 || length === 1) {
  console.log(0);
} else {
  let max = parseInt(args[2]);
  for (let i = 0; i < length; i++) {
    if (parseInt(args[i]) > max) {
      max = parseInt(args[i]);
    }
  }
  console.log(max);
}
