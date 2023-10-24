#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];


const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;


request(apiUrl, (error, response, body) => {
	if (error) {
		console.error(error);
	} else {
		const movieData = JSON.parse(body);


		for (const character of movieData.characters) {
			request(character, (charError, charResponse, charBody) => {
				if (charError) {
					console.error(charError);
				} else {
					const charData = JSON.parse(charBody);
					console.log(charData.name);
				}
			});
		}
	}
});
