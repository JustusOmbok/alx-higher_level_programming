#!/usr/bin/node
// Gets file and writes content to it

const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];


fs.writeFile(filePath, content, 'utf-8', (err) => {
	if (err) {
		console.error(err);
	}
});
