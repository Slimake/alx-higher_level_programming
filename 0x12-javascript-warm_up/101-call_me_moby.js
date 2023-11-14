#!/usr/bin/node

exports.callMeMoby = function (num, func) {
  let i = 0;
  while (i < num) {
    func();
    i++;
  }
};
