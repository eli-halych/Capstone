import React from 'react';
import './App.css';
import Login from './login/Login';
import Logout from "./login/Logout";

function App() {
  return (
    <div className="App">
        // TODO configure what to display upon login/logout
      <Login/>
      <Logout/>
    </div>
  );
}

export default App;
