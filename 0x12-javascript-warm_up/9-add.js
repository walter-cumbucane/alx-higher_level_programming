#!/usr/bin/node

const process = require('process');
const args = process.argv;

function add (a, b) {
  return (a + b);
}

console.log(add(parseInt(args[2]), parseInt(args[3])));
