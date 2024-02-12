#!/usr/bin/node

const process = require('process');
const cmdArguments = process.argv;

if (cmdArguments[2] === undefined) {
  console.log('No argument');
} else {
  console.log(cmdArguments[2]);
}
