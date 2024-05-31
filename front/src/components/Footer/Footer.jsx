import { Icons } from "../Icons/Icons";
import styles from "./Footer.module.scss";

export const Footer = (props) => {
    return (
        <footer className={styles.footer}>
            <div className={styles.brand}>
                <Icons size={160} color="white" />
                <p>Gestión integral de tu bienestar.</p>
            </div>
            <div className={styles.contact}>
                <p>Contactanos</p>
                <div className={styles.logos}>
                    <Icons icon="twitter" size={48} color="white" />
                    <Icons icon="instagram" size={48} color="white" />
                    <Icons icon="facebook" size={48} color="white" />
                </div>
            </div>
        </footer>
    );
};
