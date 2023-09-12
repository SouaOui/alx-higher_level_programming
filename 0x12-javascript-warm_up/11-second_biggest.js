#!/usr/bin/node
const args = process.argv;
args.splice(0, 2);
const newArr = args.map((num, i) => {
  return parseInt(num);
});
newArr.sort().reverse();
const length = args.length;
if (length === 0 || length === 1) {
  console.log(0);
} else {
  console.log(newArr[1]);
}
