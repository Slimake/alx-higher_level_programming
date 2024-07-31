#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) throw error;

  if (response.statusCode === 200) {
    const todos = JSON.parse(body);

    const dic = {};

    for (const i in todos) {
      if (todos[i].completed === true) {
        if (dic[todos[i].userId] === undefined) {
          dic[todos[i].userId] = 1;
        } else {
          dic[todos[i].userId]++;
        }
      }
    }

    console.log(dic);
  }
});
