import {
    BackArrow,
    Calendar,
    Comentar,
    Derma,
    DownArrow,
    Endo,
    Error404,
    Error500,
    Facebook,
    Hemo,
    Gine,
    Home,
    HomeImage,
    Image404,
    Image500,
    Instagram,
    Logo,
    Menu,
    Password,
    PasswordVisible,
    Perfil,
    Twitter,
    Search,
    Edit,
    Setting,
    Document,
    Comment,
    Close,
    Ofta,
    Lab,
    Nefro,
    Neu,
    Oto,
    Pedi,
    Toxi,
    Tra,
    Uro,
    Ale,
    Hema,
    Car,
    Neumo,
    Odo,
    Onco,
    Gastro,
} from "../../assets";

import styles from "./Icons.module.scss";

const ImagesDict = {
    facebook: Facebook,
    instagram: Instagram,
    twitter: Twitter,
    error404: Error404,
    image404: Image404,
    error500: Error500,
    image500: Image500,
    homeImage: HomeImage,
    backArrow: BackArrow,
    downArrow: DownArrow,
    menu: Menu,
    password: Password,
    passwordVisible: PasswordVisible,
    search: Search,
    edit: Edit,
    setting: Setting,
    document: Document,
    comment: Comment,
    close: Close,
    home: Home,
    perfil: Perfil,
    calendar: Calendar,
    comentar: Comentar,
    derma: Derma,
    gine: Gine,
    endo: Endo,
    hemo: Hemo,
    ofta: Ofta,
    lab: Lab,
    nefro: Nefro,
    neu: Neu,
    oto: Oto,
    pedi: Pedi,
    toxi: Toxi,
    tra: Tra,
    uro: Uro,
    ale: Ale,
    car: Car,
    hema: Hema,
    neumo: Neumo,
    odo: Odo,
    onco: Onco,
    gastro: Gastro,
};

const Icon = ({ icon, ...props }) => {
    const SelectedIcon = ImagesDict[icon] ?? Logo;

    return <SelectedIcon {...props} />;
};

export const Icons = (props) => {
    return (
        <Icon
            className={`${styles.icon} ${
                props.color ? styles[props.color] : ""
            } ${props.className}`}
            icon={props.icon}
            style={{
                width: `${props.size}px`,
                height: `${props.size}px`,
            }}
        />
    );
};
