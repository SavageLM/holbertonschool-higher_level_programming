#!/usr/bin/node
const request = require('request');
const movieUrl = process.argv[2];
request(movieUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const taskInfo = JSON.parse(body);
    const doneTasks = {};
    taskInfo.forEach((task) => {
      if (task.completed && doneTasks[task.userId] === undefined) {
        doneTasks[task.userId] = 1;
      } else if (task.completed) {
        doneTasks[task.userId] += 1;
      }
    });
  }
});
