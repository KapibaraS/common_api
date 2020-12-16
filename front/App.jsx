import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";

import { Main } from "./components/Main/Main";
import { Report } from "./components/Report/Report";
import { Header } from "./components/Header/Header";

export const App = () => (
  <BrowserRouter>
    <Header />
    <Switch>
      <Route exact path="/" component={Main} />
      <Route exact path="/report/:report_uid" component={Report} />
      <Route exact path="/project/:project_uid" component={Project} />
      <Route exact path="/matching/:report_uid" component={Matching} />
      <Route exact path="/employees_tasks/:report_uid/:legal_project_id" component={Task} />
      <Route component={NotFound} />
    </Switch>
  </BrowserRouter>
);
