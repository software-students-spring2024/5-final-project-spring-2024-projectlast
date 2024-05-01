import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Recommendations = () => {
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    const fetchRecommendations = async () => {
      try {
        const response = await axios.get('/api/recommendations');
        setRecommendations(response.data);  // Assume the response data is an array of strings
      } catch (error) {
        alert('Error fetching recommendations: ' + error.message);
      }
    };
    fetchRecommendations();
  }, []);

  return (
    <div>
      <h1>Recommendations</h1>
      {recommendations.length > 0 ? (
        <ul>
          {recommendations.map((recommendation, index) => (
            <li key={index}>{recommendation}</li>
          ))}
        </ul>
      ) : (
        <p>No recommendations available. Keep exercising to get personalized tips!</p>
      )}
    </div>
  );
}

export default Recommendations;
