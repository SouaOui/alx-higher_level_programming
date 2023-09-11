#!/usr/bin/node
const args = process.argv;
const n = parseInt(args[2]);
function factorial (n) {
  if (n === 0 || n === 1 || n === 'NaN') {
    return (1);
  }
  return n * factorial(n - 1);
}
if (!isNaN(n)) {
  console.log(factorial(n));
} else {
  console.log(1);
}
