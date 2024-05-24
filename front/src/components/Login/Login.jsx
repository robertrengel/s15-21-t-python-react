
import React from 'react';
import './Login.css';

function Login() {
  return (
    <section className="vh-100 gradient-custom">

      <div className="container py-5 h-100">

        <div className="row d-flex justify-content-center align-items-center h-100">

          <div className="col-12 col-md-8 col-lg-6 col-xl-5">

            <div className="card bg-dark text-white" style={{ borderRadius: "1rem" }}>

              <div className="card-body p-5 text-center" style={{ borderRadius: "1rem" }}>

                <div className="mb-md-5 mt-md-4 pb-5">
                  <h2 className="fw-bold mb-2 text-uppercase">Iniciar Sesión</h2>
      

                  <div data-mdb-input-init="" className="form-outline form-white mb-4">
                    <label className="form-label" htmlFor="typeEmailX"> Email </label>
                    <input type="email" id="typeEmailX" className="form-control form-control-lg"  />
                  
                    
                  </div>

                  <div data-mdb-input-init="" className="form-outline form-white mb-4" >
                    <label className="form-label" htmlFor="typePasswordX"> Contraseña </label>
                    <input type="password" id="typePasswordX" className="form-control form-control-lg" />
                    <p className="small mb-5 pb-lg-2"> Utiliza al menos 8 caracteres ,combinando letras mayúsculas
                      y minúsculas,números y caracteres especiales (como @,#,$,%). </p>
                  </div>


                  <button data-mdb-button-init="" data-mdb-ripple-init="" className="btn btn-outline-light btn-lg px-5"
                    type="submit"> Iniciar Sesión </button>

                  <p className="small mb-5 pb-lg-2"> <a className="text-white-50" href="#!">  ¿Olvidaste tu contraseña?</a> </p>
                </div>


              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

  );
}

export default Login;





