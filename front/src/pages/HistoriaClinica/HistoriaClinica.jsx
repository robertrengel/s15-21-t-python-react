import styles from './HistoriaClinica.module.scss';
import { SideBarInterno } from "../../components/SideBarInterno/SideBarInterno";
import { Footer } from '../../components/Footer/Footer';
import { Header } from '../../components/Header/Header.jsx'
import { Comentarios } from '../../components/Comentarios/Comentarios.jsx'
import { Label } from '../../components/Label/Label.jsx'

export const HistoriaClinica = () => {
    return (
        <div>
            <div className={styles.container}>
                <SideBarInterno />
                <Header />
                <Label />
                <div className={styles.especialidad}>
                    <h1 className={styles.title_especialidad}> Especialidad </h1>
                </div>
                <Comentarios />
                
            </div>
            <Footer />
        </div>
    );
};