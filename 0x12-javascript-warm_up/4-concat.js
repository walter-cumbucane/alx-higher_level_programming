#!/usr/bin/node

const process = require('process');
const cmdArgs = process.argv;

const argumentOne = cmdArgs[2];
const argumentTwo = cmdArgs[3];

console.log(argumentOne + ' is ' + argumentTwo);
