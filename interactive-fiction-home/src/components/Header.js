import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => (
  <header>
    <div className="logo">Interactive Fiction</div>
    <nav>
      <Link to="/">Home</Link>
      <Link to="/browse">Browse Stories</Link>
      <Link to="/create">Create Story</Link>
      <Link to="/profile">My Profile</Link>
    </nav>
  </header>
);

export default Header;
