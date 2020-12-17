import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { CarsList, NewCar } from './components/Cars';

const App = () => (
  <BrowserRouter>
    <Switch>
      <Route path="/cars/new" component={NewCar} />
      <Route path="/" component={CarsList} />
    </Switch>
  </BrowserRouter>
);

export default App;
