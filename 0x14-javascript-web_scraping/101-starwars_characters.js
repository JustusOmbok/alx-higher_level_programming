#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];


const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;


request(apiUrl, (error, response, body) => {
	if (error) {
		console.error(error);
	} else {
		const movieData = JSON.parse(body);

		const characterUrls = movieData.characters;


		function printCharacters(index) {
			if (index < charactersUrls.length) {
				const characterUrl = characterUrls[index];
				request(characterUrl, (charError, charResponse, charBody) => {
					if (charError) {
						console.error(charError);
					} else {
						const charData = JSON.parse(charBody);
						console.log(charData.name);
						printCharacter(index + 1);
					}
				});
			}
		}
		printCharacters(0);
	}
});
