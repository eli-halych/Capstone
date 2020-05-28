import React from 'react';
import './App.css';
import Login from './login/Login';
import Logout from "./login/Logout";
import {isAuthenticated} from "./utils/Auth";


function App() {
  return (
    <div className="App">
        { isAuthenticated() ? <Logout/> : <Login/> }
    </div>
  );
}

export default App;
