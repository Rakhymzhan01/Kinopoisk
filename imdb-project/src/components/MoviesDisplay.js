import React, { useEffect, useState } from 'react';

const MoviesDisplay = () => {
    const [movies, setMovies] = useState([]);

    useEffect(() => {
        fetch('/movies.json') // Using relative path assuming movies.json is in the public directory
            .then(response => response.json())
            .then(data => setMovies(data))
            .catch(error => console.error('Error loading the movies:', error));
    }, []);

    return (
        <div className="movies-container">
            {movies.map((movie, index) => (
                <div key={index} className="movie-display">
                    <div className="movie-image">
                        {movie.poster && <img src={movie.poster} alt={`Poster of ${movie.title}`} />}
                    </div>

                        <div className="movie-title">
                        <h2>{movie.title} {movie.year}</h2>
                            </div>
                        <div className="movie-info">
                        <p>Genre: {movie.genre}</p>
                        <p>Duration: {movie.duration}</p>
                        <p>Director: {movie.director}</p>
                        <p>Actors: {movie.actors}</p>
                        <p>Plot: {movie.plot}</p>
                        <img src={movie.image_link} alt={`Poster of ${movie.title}`} />
                    </div>
                </div>
            ))}
        </div>
    );
};

export default MoviesDisplay;
