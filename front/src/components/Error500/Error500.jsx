import React from 'react';
import './Error500.scss';
import illustration3 from '/src/assets/illustration3.png';
import illustration4 from '/src/assets/illustration4.png';

const Error500 = () => {
  return (
    <div className="error-container">
      
      <div className="illustrations">
        <img src={illustration3} alt="Illustration 3" className="illustration" />
        <img src={illustration4} alt="Illustration 4" className="illustration" />
      </div>

      
      <p>Servidor no encontrado.</p>

     


    </div>
  );
};

export default Error500;

