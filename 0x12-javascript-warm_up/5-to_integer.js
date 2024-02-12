#!/usr/bin/node

const process = require('process');
const cmdArgs = process.argv;
const arg = cmdArgs[2];

if (arg === undefined || isNaN(arg)) {
  console.log('Not a number');
} else {
  const finalNumber = parseInt(arg);
  console.log('My number: ', finalNumber);
}
