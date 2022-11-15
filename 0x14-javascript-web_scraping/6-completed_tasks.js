#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }

  const data = JSON.parse(body);
  const result = {};
  let id = 0;

  for (let i = 0; i < data.length; i++) {
    if (data[i].userId === id) {
      continue;
    } else {
      id = data[i].userId;
    }
    let tasks = 0;
    for (let j = 0; j < data.length; j++) {
      if (data[j].userId === id && data[j].completed === true) {
        tasks++;
      }
    }
    if (tasks > 0) {
      result[id] = tasks;
    }
  }
  console.log(result);
});
