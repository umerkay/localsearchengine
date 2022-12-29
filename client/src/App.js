import React, { useReducer, useEffect, useState } from "react";
import "./App.scss";
import { SearchReq } from "./Actions/Search"
import Header from "./Components/Header";
import DocsContainer from "./Components/DocContainer";
import Search from "./Components/Search";
import { Link, HashRouter as Router, Route, Switch } from 'react-router-dom';
import { reducer, initialState } from './Reducer';

const App = () => {
  const [state, dispatch] = useReducer(reducer, initialState);
  const [page, setPage] = useState(0)

  const { docs, errorMessage, loading, time, totalResults } = state;

  const baseUrl = "" //process.env.PUBLIC_URL;

  const search = (...args) => SearchReq(dispatch, ...args);

  return (
    <div className="AppContainer">
      <div className="App">
        <Router>
          <Switch>
            <Route path={baseUrl + "/"} exact render={props => (<>
              {/* <Header focus={true} /> */}
              <Search search={search} page={page} setPage={setPage}/>
            </>
            )}></Route>

            <Route path={baseUrl + "/search/:q/:page?"} render={props => (<>
              {/* <Header focus={!movies.length && !loading} /> */}
              <Search search={search} {...props} page={page} setPage={setPage}/>
              <DocsContainer
                errorMessage={errorMessage}
                docs={docs}
                loading={loading}
                search={search}
                time={time}
                totalResults={totalResults}
                page={page}
                setPage={setPage}
                {...props}
                >
              </DocsContainer>
            </>
            )}></Route>
          </Switch>
        </Router>
      </div>
    </div>
  );
};

export default App;