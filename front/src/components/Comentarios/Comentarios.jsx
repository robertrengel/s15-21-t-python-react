import styles from "./Comentarios.module.scss";
import { Input } from "../Input/Input";

export const Comentarios = () => {
  return (
    <div className={styles.container_coment}>
      <div className={styles.title_coment}>
        <h2 className={styles.title}> Marcelo perez </h2>
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
        <div className={styles.coment_field}>
        <div>
            <Input
                className={styles.este_textarea}
                type="textarea"
                placeholder="Ingresa tu comentario"
            />
        </div>
        </div>
      </div>
    </div>
  );
};
