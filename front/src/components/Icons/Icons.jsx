import { Facebook, Instagram, Logo, Twitter } from "../../assets";
import styles from "./Icons.module.scss";

const Icon = ({ icon, ...props }) => {
    let SelectedIcon;
    switch (icon) {
        case "facebook":
            SelectedIcon = Facebook;
            break;
        case "instagram":
            SelectedIcon = Instagram;
            break;
        case "twitter":
            SelectedIcon = Twitter;
            break;
        default:
            SelectedIcon = Logo;
            break;
    }

    return <SelectedIcon {...props} />;
};

export const Icons = (props) => {
    return (
        <Icon
            className={`${styles.icon} ${
                props.color ? styles[props.color] : ""
            }`}
            icon={props.icon}
            style={{
                width: `${props.size}px`,
                height: `${props.size}px`,
            }}
        />
    );
};
