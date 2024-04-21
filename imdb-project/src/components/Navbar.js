// src/components/Navbar.js
import React from 'react';
import './Navbar.css'; // Importing Navbar styles

const Navbar = () => {
  return (
    <div className="navbar">
      <a className="navbar-brand">Kinopoisk</a>
      <ul className="navbar-links">
        <li><a href="#"><i className="fas fa-home"></i> Home</a></li>
        <li><a href="#"><i className="fas fa-tv"></i> TV Shows</a></li>
        <li><a href="#"><i className="fas fa-film"></i> Movies</a></li>
        <li><a href="#"><i className="fas fa-calendar-alt"></i> Latest</a></li>
        <li><a href="#"><i className="fas fa-list"></i> My List</a></li>
      </ul>
      {/* Search box code will be here if you decide to show it */}
    </div>
  );
};

export default Navbar;
