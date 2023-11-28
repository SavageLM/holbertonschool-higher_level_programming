#!/usr/bin/node

exports.converter = function (base) {
  return numConvert => numConvert.toString(base);
};
