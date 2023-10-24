#!/usr/bin/node
//Reads the file in utf-8
const fs = require('fs');
const filePath = process.argv[2];


fs.readFile(filePath, "utf-8", (err, data) => {
	if (err) {
		console.error(err);
	} else {
		console.log(data);
	}
});