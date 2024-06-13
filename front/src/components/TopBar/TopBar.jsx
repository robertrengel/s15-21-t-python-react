import { useState } from "react";
import { Icons } from "../Icons/Icons";
import styles from "./TopBar.module.scss";
import { useNavigate } from "react-router-dom";
import { Button } from "../Button/Button";

export function TopBar(props) {
    const [seeMenu, setSeeMenu] = useState(false);
    const history = useNavigate();

    return (
        <div className={styles.topBar}>
            <div className={styles.icon}>
                {props.hasBack && (
                    <div onClick={() => history(-1)}>
                        <Icons icon="backArrow" size={30} />
                    </div>
                )}
                {props.hasMenu && (
                    <Button
                        variant="text"
                        onClick={() => setSeeMenu((visible) => !visible)}
                    >
                        <Icons icon="menu" size={30} />
                    </Button>
                )}
                {seeMenu && props.menuItems && (
                    <div className={styles.menuItem}>
                        {Object.keys(props.menuItems).map((item) => (
                            <Button
                                variant="text"
                                key={props.menuItems[item].label}
                                onClick={() => {
                                    setSeeMenu(false);
                                    props.menuItems[item].onClick();
                                }}
                            >
                                {props.menuItems[item].label}
                            </Button>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
}
