#!/usr/bin/node

const array = process.argv;
if (array[2] === undefined) {
  console.log('No argument');
} else {
  console.log(array[2]);
}
