import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import styles from './Calendario.module.scss';
import { Button } from "../../components/Button/Button";

const Calendario = () => {
  return (
    <div className="container mt-5">
      <h1 className="text-center mb-4">Nombre Profesional</h1>
      <div className={`text-white p-3 mb-4 ${styles.calendarContainer}`}>
        <h2 className={`mb-2 ${styles.calendarTitle}`}>Junio</h2>
        <div className={styles.calendarWrapper}>
          <Calendar className={styles.calendar} />
        </div>
      </div>
      <div className="d-flex justify-content-center align-items-center mb-4 gap-2">
        <span className="me-2">Hora:</span>
        <div className={`hour-box p-2 bg-light text-center rounded ${styles.hourBox}`}>08:00</div>
        <div className={`hour-box p-2 bg-light text-center rounded ${styles.hourBox}`}>10:00</div>
        <div className={`hour-box p-2 bg-light text-center rounded ${styles.hourBox}`}>12:00</div>
        <div className={`hour-box p-2 bg-light text-center rounded ${styles.hourBox}`}>14:00</div>
      </div>
      <div className="d-flex flex-column align-items-center">
        <Button variant="primary" width={300} height={40}>Label</Button>
        <Button variant="primary" width={300} height={40} className="mt-2">Label</Button>
      </div>
    </div>
  );
};

export default Calendario;
