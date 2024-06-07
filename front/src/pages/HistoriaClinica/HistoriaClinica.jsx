import styles from './HistoriaClinica.module.scss';
import { SideBarInterno } from "../../components/SideBarInterno/SideBarInterno";
import { Footer } from '../../components/Footer/Footer';
import { Input } from '../../components/Input/Input';
import { Icons } from '../../components/Icons/Icons';
import { Comentarios } from '../../components/Comentarios/Comentarios.jsx'

export const HistoriaClinica = () => {
    return (
        <div>
            <div className={styles.container}>
                <SideBarInterno />
                <div className={styles.historia_clinica}>
                    <img src='../../../public/imagenes/Ellipse 2.png' alt='Foto de Julio Diaz' />
                    <p>Julio Diaz</p>
                </div>
                <div className={styles.search_container}>
                    <div className={styles.input_with_icon}>
                        <Input type='search' placeholder='Buscar' />
                        <span className={styles.search_icon}>
                            <Icons icon="buscar" size={24} color="primary" />
                        </span>
                    </div>
                </div>
                <div className={styles.label_container}>
                    <img src='../../../public/imagenes/chip-profesionales.png' alt='' />
                    <img src='../../../public/imagenes/chip-profesionales.png' alt='' />
                    <img src='../../../public/imagenes/chip-profesionales.png' alt='' />
                    <img src='../../../public/imagenes/chip-profesionales.png' alt='' />
                    <img src='../../../public/imagenes/chip-profesionales.png' alt='' />
                </div>
                <div className={styles.especialidad}>
                    <h1 className={styles.title_especialidad}> Especialidad </h1>
                </div>
                <Comentarios />
                <Comentarios />
                <Comentarios />
            </div>
            <Footer />
        </div>
    );
};