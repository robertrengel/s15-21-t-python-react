// Acá van las importaciones.
import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Registro from './components/Registro/Registro';

const App = () => {
  // Dentro de este bloque vamos a ir definiendo las pantallas que se van a ir mostrando

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/Registro" element={<Registro />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
