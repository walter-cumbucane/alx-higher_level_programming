#!/usr/bin/node

const process = require('process');
const cmdArgs = process.argv;
const arg = cmdArgs[2];

if (isNaN(arg) || arg === undefined) {
  console.log('Not a number');
} else {
  const finalNumber = parseInt(arg);
  console.log('My number: ', finalNumber);
}
