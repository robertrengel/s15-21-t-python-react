import { Button } from "../Button/Button";
import { Icons } from "../Icons/Icons";
import styles from "./Sidebar.module.scss";

export const SideBar = (props) => {
    return (
        <aside className={styles.sideBar}>
            <div className={styles.brand}>
                <Icons size={230} color="white" />
                <p>Gestión integral de tu bienestar.</p>
            </div>
            <div className={styles.actionButtons}>
                <Button width={341} height={48} onClick={(e) => console.log(e)}>
                    Registrarse
                </Button>
                <Button width={341} height={48}>
                    Iniciar Sesion
                </Button>
            </div>
        </aside>
    );
};
