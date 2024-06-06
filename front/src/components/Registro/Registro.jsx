import React from 'react';
import styles from './Registro.module.scss';
import { Button } from '../Button/Button';

const Registro = () => {
  return (
    <div className={styles.formContainer}>
      <div className={styles.titleContainer}>
        <h2>Formulario de registro</h2>
        <hr />
      </div>
      <div className="row">
        <div className="col-sm-12 col-md-6">
          <div className={`form-group mb-4 ${styles.formRow}`}>
            <label htmlFor="nombre">Nombre</label>
            <input id="nombre" type="text" className="form-control" />
          </div>
          <div className={`form-group mb-4 ${styles.formRow}`}>
            <label htmlFor="fechaNacimiento">Fecha de Nacimiento</label>
            <input id="fechaNacimiento" type="date" className="form-control" />
          </div>
          <div className={`form-group mb-4 ${styles.formRow}`}>
            <label htmlFor="pais">País</label>
            <select className="form-select" id="pais">
              <option value="">Seleccione un país</option>
              <option value="Argentina">Argentina</option>
              <option value="Colombia">Colombia</option>
              <option value="Perú">Perú</option>
              <option value="México">México</option>
            </select>
          </div>
          <div className={`form-group mb-4 ${styles.formRow}`}>
            <label htmlFor="password">Contraseña</label>
            <input id="password" type="password" className="form-control" />
            <small className={styles.passwordMessage}>Utiliza al menos 8 caracteres, combinando letras mayúsculas y minúsculas, números y caracteres especiales (como @, #, $, %).</small>
          </div>
        </div>
        <div className="col-sm-12 col-md-6">
          <div className={`form-group mb-4 ${styles.formRow}`}>
            <label htmlFor="apellido">Apellido</label>
            <input id="apellido" type="text" className="form-control" />
          </div>
          <div className={`form-group mb-4 ${styles.formRow}`}>
            <label htmlFor="dni">Identificador nacional/DNI</label>
            <input id="dni" type="text" className="form-control" />
          </div>
          <div className={`form-group mb-4 ${styles.formRow}`}>
            <label htmlFor="email">E-mail</label>
            <input id="email" type="email" className="form-control" />
          </div>
          <div className={`form-group mb-4 ${styles.formRow}`}>
            <label htmlFor="repeatPassword">Repetir Contraseña</label>
            <input id="repeatPassword" type="password" className="form-control" />
            <small className={styles.passwordMessage}>Utiliza al menos 8 caracteres, combinando letras mayúsculas y minúsculas, números y caracteres especiales (como @, #, $, %).</small>
          </div>
        </div>
      </div>
      <div className="row mt-5">
        <div className="col-12 d-flex justify-content-center">
          <button className={`btn btn-outline-light me-3 ${styles.cancelButton}`}>Cancelar</button>
          <Button width={200} height={50}>Guardar</Button>
        </div>
      </div>
    </div>
  );
};

export default Registro;
