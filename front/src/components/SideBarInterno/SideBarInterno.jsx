import { Button } from "../Button/Button";
import { Icons } from "../Icons/Icons";
import styles from './SideBarInterno.module.scss'

export const SideBarInterno = (props) => {
    return (
        <aside className={styles.sideBar}>
            <div className={styles.brand}>
                <Icons size={230} color="white" />
                <p>Gestión integral de tu bienestar.</p>
            </div>
            <div>
                <img className={styles.img} src="../../../public/imagenes/home.png" alt="" />
                <p className={styles.p}> Inicio </p>
                <img className={styles.img} src="../../../public/imagenes/persona.png" alt="" />
                <p className={styles.p}> Mi perfil </p>
                <img className={styles.img} src="../../../public/imagenes/calendario.png" alt="" />
                <p className={styles.p}> Calendario </p>
                <img className={styles.img} src="../../../public/imagenes/comentario.png" alt="" />
                <p className={styles.p}> Comentario </p>
            </div> 
            <div className={styles.actionButtons}>
                <Button width={341} height={48} onClick={(e) => console.log(e)}>
                    Validar profesional
                </Button> 
            </div>
        </aside>
    );
};