import React from 'react';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import './App.css';
import "./static/styles/generalStyle.scss";
import {AppRoutes} from "./constants/appRoutes.ts";
import HomePage from './pages/HomePage.tsx';
import SuperdensePage from './pages/SuperdensePage.tsx';
import TeleportationPage from './pages/TeleportationPage.tsx';
import QKDPage from './pages/QKDPage.tsx';
import NavBar from './components/header/navigator.tsx';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path={AppRoutes.ROOT} element= {<><NavBar algorithm="" /><HomePage /></>} />
        <Route path={AppRoutes.SUPERDENSE} element= {<><NavBar algorithm="superdense" /><SuperdensePage /></>} />
        <Route path={AppRoutes.TELEPORTATION} element= {<><NavBar algorithm="teleportation" /><TeleportationPage /></>} />
        <Route path={AppRoutes.QKD} element= {<><NavBar algorithm="cryptography" /><QKDPage /></>} />
      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
