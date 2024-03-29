// static/js/main.js
document.addEventListener('DOMContentLoaded', function() {
    const genreSelect = document.getElementById('genre');
    const movieList = document.getElementById('movie-list');

    genreSelect.addEventListener('change', async function() {
        const genre = this.value;
        const response = await fetch(`/api/movies/${genre}`);
        const movies = await response.json();

        movieList.innerHTML = '';
        movies.forEach(movie => {
            const listItem = document.createElement('li');
            const link = document.createElement('a');
            link.href = `/movie/${movie.id}`;
            link.textContent = `${movie.title} (${movie.year})`;
            listItem.appendChild(link);
            movieList.appendChild(listItem);
        });
    });
});