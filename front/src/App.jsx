// Acá van las importaciones.
import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Registro from './components/Registro/Registro';
import Login from './components/Log-in/Log-in.css';
import Footer from './components/Footer/Footer'

const App = () => {
  // Dentro de este bloque vamos a ir definiendo las pantallas que se van a ir mostrando

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/Registro" element={<Registro />} />
        <Route path="/Log-in" element={<Login />} />
      </Routes>
      <Footer/>
    </BrowserRouter>
  );
};

export default App;