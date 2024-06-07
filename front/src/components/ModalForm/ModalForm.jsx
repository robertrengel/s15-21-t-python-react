import styles from "./ModalForm.module.scss";
import {Button} from "../Button/Button";
export const ModalForm=({title, onClose,children})=>{
    const handleSubmit = (event) => {
        event.preventDefault(); 
      };
    return (
    <div className={styles.modal_overlay}>
        <div className={styles.modal_title}>
            <h3>{title} </h3>
        </div>
        <form  onSubmit={handleSubmit} className={styles.modal_form} >
            <div className={styles.modal_content}>
            {children}
            </div>
            <div className={styles.form_btn}>
                <Button width={159} height={48} onClick={onClose} variant="text">Cancelar</Button>
                <Button width={159} height={48} onClick={(e) => console.log(e)}>Guardar</Button>
            </div>
        </form>
    </div>

    )
}