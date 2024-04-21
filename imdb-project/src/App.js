// src/App.js
import React from 'react';
import Navbar from './components/Navbar'; // Importing the Navbar component
import SearchBox from './components/SearchBox';
import MoviesDisplay from './components/MoviesDisplay';
import './App.css'; // Make sure to import any global styles you have

const App = () => {
  return (
    <div className="app">
      <Navbar /> {/* Using the Navbar component */}
      <main>
        <SearchBox />
        <MoviesDisplay /> {/* The main content of your app */}
      </main>
    </div>
  );
};

export default App;
