import styles from "./Comentarios.module.scss";
import { Input } from "../Input/Input";
import { Button } from "../../components/Button/Button";

export const Comentarios = () => {
  return (
    <div className={styles.general_container}>

    <div className={styles.container_coment}>
  
      <div className={styles.title_coment}>
        <h2 className={styles.title}>Marcelo Perez</h2>
        <img
          className={styles.img}
          src="../../../public/imagenes/fecha.png"
          alt="11/10/23"
        />
        <img
          className={styles.mensaje}
          src="../../../public/imagenes/mensaje.png"
          alt="11/10/23"
        />
      </div>
  
      <div className={styles.coment_field}>
        <div>
          <Input
            className={styles.este_textarea}
            type="textarea"
            placeholder="Ingresa tu comentario"
          />
        </div>
      </div>
  
      <div className={styles.container_diagnosis}>
        <img
          className={styles.diagnostico}
          src="../../../public/imagenes/boton-diagnostico.png"
          alt=""
        />
      </div>
  
      <div className={styles.button_keep}>
        <Button width={159} height={48}>
          <img
            className={styles.mensaje}
            src="../../../public/imagenes/mensaje.png"
            alt="11/10/23"
          />
          Guardar
        </Button>
      </div> 
  
    </div>
  </div>

  );
};