#!/usr/bin/node
const request = require('request')
const apiUrl = process.argv[2];


request(apiUrl, (error, response, body) => {
	if (error) {
		console.error(error);
	} else {
		if (response.statusCode === 200) {
			const filmsData = JSON.parse(body);
			const characterId= 18;
			const moviesWithWedge = filmsData.results.filter((film) =>
				film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
			);
			console.log(moviesWithWedge.length);
		} else {
			console.error(`Failed to retrieve movie data. Status code: ${response.statusCode}`);
		}
	}
});
