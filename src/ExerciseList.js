import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ExerciseList = () => {
  const [exercises, setExercises] = useState([]);

  useEffect(() => {
    const fetchExercises = async () => {
      try {
        const response = await axios.get('/api/exercises');
        setExercises(response.data);
      } catch (error) {
        alert('Error fetching exercises: ' + error.message);
      }
    };
    fetchExercises();
  }, []);

  return (
    <div>
      <h1>Logged Exercises</h1>
      {exercises.length > 0 ? (
        <ul>
          {exercises.map((exercise, index) => (
            <li key={index}>{exercise.type} for {exercise.duration} minutes</li>
          ))}
        </ul>
      ) : (
        <p>No exercises logged yet.</p>
      )}
    </div>
  );
}

export default ExerciseList;
