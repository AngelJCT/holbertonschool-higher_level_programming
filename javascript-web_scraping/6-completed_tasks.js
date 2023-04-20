#!/usr/bin/node
// script that computes the number of tasks completed by user id.
const request = require('request');
const url = process.argv[2];
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const tasks = JSON.parse(body);
  const completedTasks = {};
  tasks.forEach(task => {
    if (task.completed === true) {
      if (completedTasks[task.userId] === undefined) {
        completedTasks[task.userId] = 1;
      } else {
        completedTasks[task.userId]++;
      }
    }
  });
  console.log(completedTasks);
});
