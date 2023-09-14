#!/usr/bin/node
exports.esrever = function (list) {
  const esreverList = [];
  let j = 0;
  const length = list.length;
  for (let i = length - 1; i >= 0; i--) {
    esreverList[j] = list[i];
    j++;
  }
  return esreverList;
};
