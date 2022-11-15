#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }

  const data = JSON.parse(body).results;
  let appearances = 0;

  for (let i = 0; i < data.length; i++) {
    const chars = data[i].characters;
    for (let j = 0; j < chars.length; j++) {
      if (chars[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
        appearances++;
      }
    }
  }

  console.log(appearances);
});
