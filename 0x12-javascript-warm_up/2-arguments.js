#!/usr/bin/node

const process = require('process');
const cmdArguments = process.argv;

if (cmdArguments.length === 2) {
  console.log('No argument');
} else if (cmdArguments.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
