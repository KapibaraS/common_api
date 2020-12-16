import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import {NotFound} from "./components/NotFound/NotFound";


export const App = () => (
    <BrowserRouter>
    {/*<Header />*/}
        <Switch>
          <Route exact path="/" component={NotFound} />
          <Route exact path="/v1/create_car" component={} />
          {/*<Route exact path="/v1/get_car/:car_id" component={Project} />*/}
          {/*<Route exact path="/v1/delete_car/:car_id" component={Matching} />*/}
          {/*<Route exact path="/v1/get_cars/:page" component={Task} />*/}
          {/*<Route component={NotFound} />*/}
        </Switch>
  </BrowserRouter>
);
