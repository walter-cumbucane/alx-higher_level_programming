#!/usr/bin/node

module.exports.esrever = function (list) {
  const newList = [];
  const len = list.length;
  for (let i = len - 1; i > 0; i--) {
    newList[len - 1 - i] = list[i];
  }
  return newList;
};
