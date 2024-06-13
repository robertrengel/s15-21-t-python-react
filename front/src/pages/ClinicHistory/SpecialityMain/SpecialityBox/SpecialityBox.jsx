import { Icons } from "../../../../components/Icons/Icons";
import styles from "./SpecialityBox.module.scss";

export function SpecialityBox({ speciality }) {
    return (
        <div className={styles.specialityBox}>
            <Icons size={50} icon={speciality.icon} />
            <p>{speciality.label}</p>
        </div>
    );
}
