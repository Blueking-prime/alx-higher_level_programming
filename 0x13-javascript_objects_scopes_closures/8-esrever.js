#!/usr/bin/node
exports.esrever = function (list) {
  for (let i = 0, j = list.length - 1; i < list.length / 2; i++, j--) {
    const tmp = list[j];
    list[j] = list[i];
    list[i] = tmp;
  }
  return list;
};
