import React from 'react';
import './App.css';
import Login from './login/Login';
import {isAuthenticated} from "./utils/Auth";
import Home from "./hackathons/Home";

function App() {
  return (
    <div className="App">
        { isAuthenticated()? <Home/> : <Login/> }
    </div>
  );
}

export default App;
