import styles from "./AppSideBar.module.scss";
import { Button } from "../Button/Button";
import { Icons } from "../Icons/Icons";
import { getMediaQuery } from "../../helpers/browser";
import { useNavigate } from "react-router-dom";

const getIconSize = () => {
    const media = getMediaQuery();

    switch (media) {
        case "small":
            return 64;
        case "medium":
            return 250;
        default:
            return 220;
    }
};

export function AppSideBar(props) {
    return (
        <div className={styles.appSideBar}>
            <div className={styles.brand}>
                <Icons size={getIconSize} color="white" />
            </div>
            <div className={styles.menu}>
                {Object.keys(props.menuItems).map((key) => (
                    <Button key={key} variant="text">
                        <Icons size={40} icon={props.menuItems[key].icon} />
                        <p>{props.menuItems[key].label}</p>
                    </Button>
                ))}
            </div>
            <div className={styles.actionButtons}>
                <Button width={341} height={48} onClick={props.onInit}>
                    Validar profesional
                </Button>
            </div>
        </div>
    );
}
