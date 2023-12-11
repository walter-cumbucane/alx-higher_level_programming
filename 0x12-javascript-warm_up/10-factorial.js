#!/usr/bin/node

const process = require('process');
const args = process.argv;

let fact = 0;
function factorial (n) {
  if (n === 0) {
    return (1);
  }
  fact = n * factorial(n - 1);
  return (fact);
}

if (args[2] === undefined) {
  console.log(1);
} else {
  console.log(factorial(parseInt(args[2])));
}
