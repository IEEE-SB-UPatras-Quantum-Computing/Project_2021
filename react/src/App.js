import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import NavBar from './components/navigator';
import Home from './components/home';
import Superdense from './components/superdense';
import Teleport from './components/teleportation';
import QCryptography from './components/cryptography';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>

        <Route exact path='/' element= {<><NavBar algorithm="" /><Home /></>} />
        <Route exact path='/superdense' element= {<><NavBar algorithm="superdense" /><Superdense /></>} />
        <Route exact path='/teleportation' element= {<><NavBar algorithm="teleportation" /><Teleport /></>} />
        <Route exact path='/cryptography' element= {<><NavBar algorithm="cryptography" /><QCryptography /></>} />

      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
