import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { CarsList, EditCar, NewCar } from './components/Cars';

const App = () => (
  <BrowserRouter>
    <Switch>
      <Route path="/cars/:id/edit" component={EditCar} />
      <Route path="/cars/new" component={NewCar} />
      <Route path="/" component={CarsList} />
    </Switch>
  </BrowserRouter>
);

export default App;
