#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }

  const data = JSON.parse(body);
  const result = {};

  for (let i = 1; i <= 10; i++) {
    let tasks = 0;
    for (let j = 0; j < data.length; j++) {
      if (data[j].userId === i && data[j].completed === true) {
        tasks++;
      }
    }
    if (tasks > 0) {
      result[i] = tasks;
    }
  }
});
