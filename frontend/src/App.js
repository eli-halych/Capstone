import React from 'react';
import './App.css';
import Login from './login/Login';
import Logout from "./login/Logout";

function App() {
    // TODO configure what to display upon login/logout
    // TODO implement that in NavBar
  return (
    <div className="App">
      <Login/>
      <Logout/>
    </div>
  );
}

export default App;
