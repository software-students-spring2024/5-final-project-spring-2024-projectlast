import React from 'react';
import { render, fireEvent, waitFor } from '@testing-library/react';
import App from './App';
import Dashboard from './Dashboard';
import ExerciseLogForm from './ExerciseLogForm';
import ExerciseList from './ExerciseList';
import StatsView from './StatsView';
import Recommendations from './Recommendations';
import axios from 'axios';

jest.mock('axios');

describe('Fitness Tracker Application', () => {

  describe('Dashboard Component', () => {
    test('renders welcome message', () => {
      const { getByText } = render(<Dashboard />);
      expect(getByText(/Welcome to Your Fitness Tracker/i)).toBeInTheDocument();
    });
  });

  describe('ExerciseLogForm Component', () => {
    test('submits exercise data', async () => {
      axios.post.mockResolvedValue({ data: { message: 'Exercise logged' } });

      const { getByLabelText, getByRole } = render(<ExerciseLogForm />);
      fireEvent.change(getByLabelText(/Type of Exercise:/i), { target: { value: 'Cardio' } });
      fireEvent.change(getByLabelText(/Duration \(in minutes\):/i), { target: { value: '30' } });
      fireEvent.click(getByRole('button'));

      await waitFor(() => {
        expect(axios.post).toHaveBeenCalledWith('/api/exercises', {
          type: 'Cardio',
          duration: '30'
        });
      });
    });
  });

  describe('ExerciseList Component', () => {
    test('fetches and displays exercises', async () => {
      const exercises = [{ type: 'Cardio', duration: 30 }, { type: 'Strength', duration: 20 }];
      axios.get.mockResolvedValue({ data: exercises });

      const { findByText } = render(<ExerciseList />);
      const cardioText = await findByText(/Cardio for 30 minutes/i);
      const strengthText = await findByText(/Strength for 20 minutes/i);

      expect(cardioText).toBeInTheDocument();
      expect(strengthText).toBeInTheDocument();
    });
  });

  describe('StatsView Component', () => {
    test('fetches and displays statistics', async () => {
      const stats = {
        totalExercises: 10,
        totalMinutes: 120,
        breakdown: { Cardio: 60, Strength: 40, Flexibility: 20 }
      };
      axios.get.mockResolvedValue({ data: stats });

      const { findByText } = render(<StatsView />);
      const totalExercisesText = await findByText(/Total Exercises Logged: 10/i);
      const totalMinutesText = await findByText(/Total Exercise Minutes: 120/i);

      expect(totalExercisesText).toBeInTheDocument();
      expect(totalMinutesText).toBeInTheDocument();
    });
  });

  describe('Recommendations Component', () => {
    test('fetches and displays recommendations', async () => {
      const recommendations = [
        "Increase your Cardio sessions",
        "Consider more Strength training"
      ];
      axios.get.mockResolvedValue({ data: recommendations });

      const { findByText } = render(<Recommendations />);
      const cardioRec = await findByText(/Increase your Cardio sessions/i);
      const strengthRec = await findByText(/Consider more Strength training/i);

      expect(cardioRec).toBeInTheDocument();
      expect(strengthRec).toBeInTheDocument();
    });
  });

});

