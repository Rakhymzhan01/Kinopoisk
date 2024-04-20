import React, { useEffect, useState } from 'react';
import './MovieDisplay.css';

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
            <img src={movie.image_link} alt={`Poster of ${movie.title}`} className="movie-poster" />
          </div>
          <div className="movie-info">
            <h2 className="movie-title">{movie.title} ({movie.year})</h2>
            <p className="movie-genre">Genre: {movie.genre}</p>
            <p className="movie-duration">Duration: {movie.duration}</p>
            <p className="movie-director">Director: {movie.director}</p>
            <p className="movie-actors">Actors: {movie.actors}</p>
            <p className="movie-plot">Plot: {movie.plot}</p>
          </div>
        </div>
      ))}
    </div>
  );
};

export default MoviesDisplay;