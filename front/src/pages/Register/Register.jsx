import { useEffect, useState } from "react";
import { TopBar } from "../../components/TopBar/TopBar";
import styles from "./Register.module.scss";
import { Form } from "./Form/Form";
import { getCountriesList } from "../../services/apiLists";
import { Loader } from "../../components/Loader/Loader";

const FormFields = {
    nombre: {
        label: "Nombre",
        value: "",
    },
    apellido: {
        label: "Apellido",
        value: "",
    },
    nacimiento: {
        label: "Fecha de nacimiento",
        type: "date",
        value: "",
    },
    dni: {
        label: "Identificador nacional",
        value: "",
    },
    pais: {
        label: "Pais",
        type: "select",
        options: [
            { label: "Argentina", value: "AR" },
            { label: "Colombia", value: "CO" },
            { label: "Inactivo", value: "I" },
        ],
        value: "",
    },
    email: {
        label: "Email",
        type: "email",
        value: "",
        validation: "^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+[.]+[a-zA-Z]{2,})$",
        error: false,
    },
    password: {
        label: "Contraseña",
        type: "password",
        value: "",
        helperText:
            "Utiliza al menos 8 caracteres, combinando letras mayúsculas y minúsculas, números y caracteres especiales (como @, #, $, %).",
        validation:
            "^(?=.*[0-9])(?=.*[A-Z])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}$",
        error: false,
    },
    password_1: {
        label: "Repetir contraseña",
        type: "password",
        value: "",
        helperText:
            "Utiliza al menos 8 caracteres, combinando letras mayúsculas y minúsculas, números y caracteres especiales (como @, #, $, %) y debe coincidir con la contraseña.",
        error: false,
    },
};

export function Register(props) {
    const [countriesList, setCountriesList] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        async function getCountries() {
            try {
                setIsLoading(true);
                const response = await getCountriesList();
                const mappedValues = response.map((resp) => {
                    return { value: resp.code, label: resp.name.trim() };
                });
                setCountriesList(mappedValues);
                setIsLoading(false);
            } catch (e) {
                console.error(e);
                setIsLoading(false);
            }
        }

        getCountries();
    }, []);

    return (
        <>
            <TopBar hasBack />
            <div className={styles.register}>
                {!isLoading && (
                    <Form
                        title="Formulario de registro"
                        fields={{
                            ...FormFields,
                            pais: {
                                ...FormFields["pais"],
                                options: countriesList,
                            },
                        }}
                    />
                )}
                {isLoading && <Loader isLoading={isLoading} />}
            </div>
        </>
    );
}
