import React from 'react';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import './App.css';
import NavBar from './components/navigator.tsx';
import Home from './components/home.tsx';
import Superdense from './components/superdense.tsx';
import Teleport from './components/teleportation.tsx';
import QCryptography from './components/cryptography.tsx';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path='/' element= {<><NavBar algorithm="" /><Home /></>} />
        <Route path='/superdense' element= {<><NavBar algorithm="superdense" /><Superdense /></>} />
        <Route path='/teleportation' element= {<><NavBar algorithm="teleportation" /><Teleport /></>} />
        <Route path='/cryptography' element= {<><NavBar algorithm="cryptography" /><QCryptography /></>} />
      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
