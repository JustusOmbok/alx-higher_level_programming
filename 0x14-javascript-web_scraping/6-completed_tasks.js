#!/usr/bin/node
//Gets ids that have tasks completed
const request = require('request');
const apiUrl = process.argv[2];


request(apiUrl, (error, response, body) => {
	if (error) {
		console.error(error);
	} else {
		const todos = JSON.parse(body);


		const completedTasksByUser = {};


		for (const todo of todos) {
			if (todo.completed) {
				if (completedTasksByUser[todo.userId]) {
					completedTasksByUser[todo.userId]++;
				} else {
					completedTasksByUser[todo.userId] = 1;
				}
			}
		}
		console.log(completedTasksByUser);
	}
});
