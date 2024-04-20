import React from 'react';
import SearchBox from './components/SearchBox';
import MoviesDisplay from './components/MoviesDisplay';
import './App.css';

const App = () => {
  return (
    <div className="app">
      <div className="navbar">
        <h1>Kinopoisk</h1>
        <SearchBox />
      </div>
      <MoviesDisplay />  {/* Include MoviesDisplay in the layout */}
    </div>
  );
};

export default App;
