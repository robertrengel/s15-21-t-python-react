import styles from "./Comentarios.module.scss";
import { Input } from "../Input/Input";
import { Button } from "../../components/Button/Button";

export const Comentarios = ({
  userName = "Macerlo Perez",
  fecha = "11/10/23",
  mensaje = "Comentario",
}) => {
  
  {/* const getIconsSize = () => {
    const media = getIconsQuert(); 
    switch(media) {
      case 'botonDiagnostico': 
        return;
    };
  }; */} 
  
  return (
    <div className={styles.general_container}>
      <div className={styles.container_coment}>
        <div className={styles.title_coment}>
          <h2 className={styles.title}>{userName}</h2>
          <span> {fecha} </span>
          {/* <p> {mensaje} </p> */}
          <img
            src="../../../public/imagenes/mensaje.png" 
            alt="" 
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

        <div>
          <label htmlFor="upload">
            {/* <Icons Icon='botonDiagnostico' size={getIconsSize} /> */} 
            <input type="file" id="upload" style={{ display: 'none' }} />
          </label>
        </div>

        <div className={styles.button_keep}>
          <Button width={159} height={48}>
            <img
              className={styles.mensaje}
              src="../../../public/imagenes/mensaje.png"
              alt="Mensaje icono"
            />
            Guardar
          </Button>
        </div>

      </div>
    </div>
  );
};





{/* <label for="upload">
      <span class="glyphicon glyphicon-folder-open" aria-hidden="true"></span>
      <input type="file" id="upload" style="display:none">
</label> */}