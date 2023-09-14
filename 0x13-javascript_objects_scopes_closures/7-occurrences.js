#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let NumOccurence = 0;
  let i = 0;
  while (i < list.length) {
    if (list[i] === searchElement) { NumOccurence += 1; }
    i++;
  }
  return NumOccurence;
};
