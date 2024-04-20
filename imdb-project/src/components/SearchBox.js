import React, { useState } from 'react';
import axios from 'axios';
import './SearchBox.css';

const SearchBox = () => {
    const [query, setQuery] = useState('');
    const [movie, setMovie] = useState(null);
    const [error, setError] = useState('');

    const searchMovie = async () => {
        if (!query) {
            setError("Please enter a search term.");
            setMovie(null);
            return;
        }

        try {
            const response = await axios.get(`https://www.omdbapi.com/?apikey=711716bd&t=${query}`);
            if (response.data.Response === "True") {
                setMovie(response.data);
                setError('');
            } else {
                setError(response.data.Error);
                setMovie(null);
            }
        } catch (err) {
            setError('Failed to fetch data.');
            console.error('Error fetching movie:', err);
        }
    };

    return (
        <div className="search-container">
            <input
                type="text"
                className="search-input"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                onKeyPress={(e) => { if (e.key === 'Enter') searchMovie(); }}
                placeholder="Enter movie title..."
            />
            <button className="search-button" onClick={searchMovie}>Search</button>
            {error && <div className="error-message">{error}</div>}
            {movie && (
                <div className="movie-container">
                    {movie.Poster !== "N/A" && (
                        <img src={movie.Poster} alt={`Poster of ${movie.Title}`} className="movie-poster" />
                    )}
                    <div className="movie-details">
                        <h2>{movie.Title} ({movie.Year})</h2>
                        <p>{movie.Genre}</p>
                        <p>Director: {movie.Director}</p>
                        <p>Actors: {movie.Actors}</p>
                        <p>{movie.Plot}</p>
                    </div>
                </div>
            )}
        </div>
    );
};

export default SearchBox;