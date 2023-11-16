#!/usr/bin/node

exports.esrever = function (list) {
  let j = 0;
  const revList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    revList[j++] = list[i];
  }
  return revList;
};
