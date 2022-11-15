#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
