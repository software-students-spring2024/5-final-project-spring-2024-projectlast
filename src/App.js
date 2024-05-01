import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './Navbar';
import Dashboard from './Dashboard';
import ExerciseLogForm from './ExerciseLogForm';
import ExerciseList from './ExerciseList';
import StatsView from './StatsView';
import Recommendations from './Recommendations';

function App() {
  return (
    <Router>
      <Navbar />
      <div className="container">
        <Switch>
          <Route path="/" exact component={Dashboard} />
          <Route path="/log-exercise" component={ExerciseLogForm} />
          <Route path="/exercises" component={ExerciseList} />
          <Route path="/stats" component={StatsView} />
          <Route path="/recommendations" component={Recommendations} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
