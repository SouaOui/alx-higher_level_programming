#!/usr/bin/node
const args = process.argv;
args.splice(0, 2).sort();
const length = args.length;
if (length === 0 || length === 1) {
  console.log(0);
} else {
  console.log(args[length - 2]);
}
