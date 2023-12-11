#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  args.sort((a, b) => a - b);
  const number = args.length;
  console.log(args[number - 2]);
}
