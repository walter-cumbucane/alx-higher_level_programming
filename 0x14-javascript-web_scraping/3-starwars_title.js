#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = 'https://swapi.alx-tools.com/api/films'.concat(id);
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  body = JSON.parse(body);
  console.log(`${body.title}`);
});
