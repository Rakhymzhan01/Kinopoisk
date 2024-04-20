// App.js
import React from 'react';
import SearchBox from './components/SearchBox';
import MoviesDisplay from './components/MoviesDisplay';
import './App.css';

const App = () => {
  return (
    <div className="app">
      <header className="header">
        <h1 className="title">Kinopoisk</h1>
        <SearchBox />
      </header>
      <main>
        <MoviesDisplay /> {/* The main content of your app */}
      </main>
    </div>
  );
};

export default App;
