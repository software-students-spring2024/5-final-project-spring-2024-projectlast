import React, { useState, useEffect } from 'react';
import axios from 'axios';

const StatsView = () => {
  const [stats, setStats] = useState({
    totalExercises: 0,
    totalMinutes: 0,
    breakdown: {}
  });

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await axios.get('/api/stats');
        setStats(response.data);  // Assuming the response data is structured appropriately
      } catch (error) {
        alert('Error fetching statistics: ' + error.message);
      }
    };
    fetchStats();
  }, []);

  return (
    <div>
      <h1>Exercise Statistics</h1>
      <p>Total Exercises Logged: {stats.totalExercises}</p>
      <p>Total Exercise Minutes: {stats.totalMinutes}</p>
      <h2>Minutes by Type:</h2>
      {stats.breakdown && Object.keys(stats.breakdown).map((type, index) => (
        <p key={index}>{type}: {stats.breakdown[type]} minutes</p>
      ))}
    </div>
  );
}

export default StatsView;
