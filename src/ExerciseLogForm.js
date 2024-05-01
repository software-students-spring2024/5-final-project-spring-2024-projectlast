import React, { useState } from 'react';
import axios from 'axios';

const ExerciseLogForm = () => {
  const [exercise, setExercise] = useState({ type: '', duration: 0 });

  const handleChange = (e) => {
    setExercise({ ...exercise, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/exercises', exercise);
      alert('Exercise logged successfully!');
      setExercise({ type: '', duration: 0 }); // Reset the form
    } catch (error) {
      alert('Error logging exercise: ' + error.message);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>Type of Exercise:
        <select name="type" value={exercise.type} onChange={handleChange}>
          <option value="">Select a type</option>
          <option value="Cardio">Cardio</option>
          <option value="Strength">Strength</option>
          <option value="Flexibility">Flexibility</option>
        </select>
      </label>
      <label>Duration (in minutes):
        <input type="number" name="duration" value={exercise.duration} onChange={handleChange} />
      </label>
      <button type="submit">Log Exercise</button>
    </form>
  );
}

export default ExerciseLogForm;
