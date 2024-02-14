#!/usr/bin/node

module.exports.nbOccurences = function (list, searchElement) {
  const len = list.length;
  let occ = 0;
  for (let i = 0; i < len; i++) {
    if (searchElement === list[i]) {
      occ++;
    }
  }
  return occ;
};
