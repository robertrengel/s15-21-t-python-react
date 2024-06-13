import { SpecialityBox } from "./SpecialityBox/SpecialityBox";
import styles from "./SpecialityMain.module.scss";

const specialities = {
    alergia: {
        label: "Alerjología",
        icon: "ale",
        visible: false,
    },
    cardio: {
        label: "Cardiología",
        icon: "car",
        visible: false,
    },
    derma: {
        label: "Dermatología",
        icon: "derma",
        visible: false,
    },
    endo: {
        label: "Endocrinología",
        icon: "endo",
        visible: false,
    },
    gine: {
        label: "Ginecología",
        icon: "gine",
        visible: false,
    },
    gastro: {
        label: "Gastroenterología",
        icon: "gastro",
        visible: false,
    },
    hemo: {
        label: "Hemoterapia",
        icon: "hemo",
        visible: false,
    },
    hema: {
        label: "Hematología",
        icon: "hema",
        visible: false,
    },
    lab: {
        label: "Laboratorio",
        icon: "lab",
        visible: false,
    },
    neuro: {
        label: "Neurología",
        icon: "neu",
        visible: false,
    },
    neumo: {
        label: "Neumonología",
        icon: "neumo",
        visible: false,
    },
    nefro: {
        label: "Nefrología",
        icon: "nefro",
        visible: false,
    },
    ofta: {
        label: "Oftalmología",
        icon: "ofta",
        visible: false,
    },
    odon: {
        label: "Odontología",
        icon: "odo",
        visible: false,
    },
    onco: {
        label: "Oncología",
        icon: "onco",
        visible: false,
    },
    otor: {
        label: "Otorrino",
        icon: "oto",
        visible: false,
    },
    pedi: {
        label: "Pediatría",
        icon: "pedi",
        visible: false,
    },
    trauma: {
        label: "Traumatología",
        icon: "tra",
        visible: false,
    },
    toxi: {
        label: "Toxicología",
        icon: "toxi",
        visible: false,
    },
    uro: {
        label: "Urología",
        icon: "uro",
        visible: false,
    },
};

export function SpecialityMain() {
    return (
        <div className={styles.specialityMain}>
            <h2>Especialidades</h2>
            <div className={styles.content}>
                {Object.keys(specialities).map((key) => (
                    <SpecialityBox key={key} speciality={specialities[key]} />
                ))}
            </div>
        </div>
    );
}
