import { useState } from 'react';
import { Icons } from '../Icons/Icons';
import { FormContact } from '../../pages/FormContact/FormContact.jsx';
import { Button } from '../Button/Button.jsx';
import styles from './Footer.module.scss';

//import { Error404 } from '../Error404/Error404'

export const Footer = (props) => {
    const [formVisible, setFormVisible] = useState(false);

    const handleButtonFormVisible = () => {
        setFormVisible(!formVisible);
    };

    const handleCloseForm = () => {
        setFormVisible(false);
    };

    return (
        <footer className={styles.footer}>
            <div className={styles.brand}>
                <Icons size={160} color="white" />
                <p>Gestión integral de tu bienestar.</p>
            </div>
            <div className={styles.contact}>
                <div className={styles.logos}>
                    <Icons icon="twitter" size={48} color="white" />
                    <Icons icon="instagram" size={48} color="white" />
                    <Icons icon="facebook" size={48} color="white" />
                </div>
                <Button width={341} height={48} onClick={handleButtonFormVisible}>
                    Contáctanos
                </Button>
            </div>
            <FormContact isVisible={formVisible} onClose={handleCloseForm} />
        </footer>
    );
};