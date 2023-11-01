$(document).ready(function() {
    // Waits for doc to be ready
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
        const movies = data.results;
        const listMovies = $("#list_movies");

        movies.forEach(function(movie) {
            const movieTitle = $("<li>").text(movie.title);
            listMovies.append(movieTitle);
        });
    });
})