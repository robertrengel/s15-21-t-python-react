import { useContext, useEffect, useState } from "react";
import { AppSideBar } from "../../components/AppSideBar/AppSideBar";
import { Footer } from "../../components/Footer/Footer";
import { Loader } from "../../components/Loader/Loader";
import { TopBar } from "../../components/TopBar/TopBar";
import styles from "./ClinicHistory.module.scss";
import { getProfile } from "../../services/userServices";
import { SpecialityMain } from "./SpecialityMain/SpecialityMain";

export function ClinicHistory() {
    const user = JSON.parse(localStorage.getItem("user"));
    const [isLoading, setIsLoading] = useState(false);

    const menuItems = {
        home: {
            icon: "home",
            label: "Inicio",
            onClick: () => {},
        },
        perfil: {
            icon: "user",
            label: "Mi Perfil",
            onClick: () => {},
        },
        calendario: {
            icon: "calendar",
            label: "Calendario",
            onClick: () => {},
        },
        comentarios: {
            icon: "comments",
            label: "Comentarios",
            onClick: () => {},
        },
    };

    useEffect(() => {
        async function getUser() {
            try {
                setIsLoading(true);
                const response = await getProfile(
                    user["user_id"],
                    user["access_token"]
                );
                setIsLoading(false);
            } catch (e) {
                console.error(e);
                setIsLoading(false);
            }
        }

        getUser();
    }, []);

    return (
        <div className={styles.clinicHistory}>
            {isLoading && <Loader isLoading={isLoading} />}
            {!isLoading && (
                <>
                    <TopBar hasMenu menuItems={menuItems} />
                    <AppSideBar menuItems={menuItems} />
                    <SpecialityMain />
                    <Footer className={styles.footer} />
                </>
            )}
        </div>
    );
}
