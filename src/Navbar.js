import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/log-exercise">Log Exercise</Link></li>
        <li><Link to="/exercises">View Exercises</Link></li>
        <li><Link to="/stats">View Stats</Link></li>
        <li><Link to="/recommendations">Recommendations</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
