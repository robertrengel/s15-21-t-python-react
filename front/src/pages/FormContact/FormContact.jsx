import { Input } from '../../components/Input/Input.jsx';
import { Button } from '../../components/Button/Button.jsx';
import styles from './FormContact.module.scss'; 

export const FormContact = ({ isVisible, onClose, submit }) => {
  if (!isVisible) return null;

  return (
    <div className="modal-overlay">
      <div className={styles.container}>
        <div className={styles.container_text}>
          <h1 className={styles.title1}>Contacto</h1>
          <br />
          <h2 className={styles.title2}>¡Estamos aquí para ayudarte!</h2>
          <p className={styles.title3}>
            Ponte en contacto con nosotros si tienes alguna <br />
            pregunta, comentario o sugerencia.
          </p>

          <div className={styles.container_form}>
            <form className={styles.form} onSubmit={submit}>
              <Input type='input' label="Consulta" placeholder='Ingrese su consulta' />
              <Input type='textarea' label="Consulta" placeholder='Ingrese su consulta' />
            </form>
          </div>
          <Button width={341} height={48} onClick={submit}>
            Enviar
          </Button>

          <div className={styles.datos_container}>
            <div className={styles.datos_item}>
              <img
                className={styles.datos_img}
                src="../../../public/imagenes/telefono.png"
                alt="123 456 789"
              />
              <p className={styles.datos_text}>123 456 789</p>
            </div>
            <div className={styles.datos_item}>
              <img
                className={styles.datos_img}
                src="../../../public/imagenes/Email.png"
                alt="doc360@info.com"
              />
              <p className={styles.datos_text}>doc360@info.com</p>
            </div>
            <div className={styles.datos_item}>
              <img
                className={styles.datos_img}
                src="../../../public/imagenes/Direccion.png"
                alt="Direccion 123 - Argentina"
              />
              <p className={styles.datos_text}>Direccion 123 - Argentina</p>
            </div>
          </div>

          <div className={styles.modal_content}>
            <Button width={341} height={48} onClick={onClose}>
              Cerrar
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
};