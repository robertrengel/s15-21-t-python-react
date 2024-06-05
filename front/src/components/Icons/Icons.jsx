import { 
    Facebook,
    Instagram, 
    Logo, 
    Twitter,
    Urologia,
    Traumatologia,
    Toxicologia,
    Telefono,
    Sobre,
    Perfil,
    Pediatra,
    Otorrino,
    Oncologia,
    OjoAbierto,
    OjoCerrado,
    Oftalmologia,
    Odontologia,
    Neurologia,
    Neumologia,
    Nefrologia,
    Mundo,
    Laboratirio,
    Home,
    Hemoterapia,
    Hematologia,
    Ginecologia,
    Gastro,
    Endocrinologia,
    Editar,
    Dropdown,
    Dermatologia,
    Documento,
    Configuracion,
    Comentar,
    Buscar

    } from "../../assets";

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
        case "urologia":
            SelectedIcon = Urologia;
                break;
        case "traumatologia":
            SelectedIcon = Traumatologia;
            break;
         case "toxicologia":
            SelectedIcon = Toxicologia;
            break;
        case "telefono":
            SelectedIcon =  Telefono;
            break;
        case "sobre":
            SelectedIcon = Sobre;
            break;
        case "perfil":
            SelectedIcon =Perfil;
            break; 
        case "pediatra":
            SelectedIcon =Pediatra;
            break;    
        case "otorrino":
            SelectedIcon =Otorrino;
            break;  
        case "oncologia":
            SelectedIcon =Oncologia;
            break;
        case "ojoCerrado":
            SelectedIcon =OjoCerrado;
            break;
        case "ojoAbierto":
            SelectedIcon =OjoAbierto;
            break;
        case "oftalmologia":
            SelectedIcon =Oftalmologia;
            break;
        case "odontologia":
            SelectedIcon =Odontologia;
            break;
        case "neurologia":
            SelectedIcon =Neurologia;
            break;
        case "neumologia":
            SelectedIcon =Neumologia;
            break;
        case "nefrologia":
            SelectedIcon =Nefrologia;
            break;
        case "mundo":
            SelectedIcon =Mundo;
            break;
        case "laboratirio":
            SelectedIcon =Laboratirio;
            break;
        case "home":
            SelectedIcon = Home;
            break;
        case "hemoterapia":
            SelectedIcon =Hemoterapia;
            break;
        case "hematologia":
            SelectedIcon =Hematologia;
            break;
        case "ginecologia":
            SelectedIcon =Ginecologia;
            break;
        case "gastro":
            SelectedIcon =Gastro;
            break;
        case "endocrinologia":
            SelectedIcon =Endocrinologia;
            break;
        case "editar":
            SelectedIcon =Editar;
            break;
        case "dropdown":
            SelectedIcon =Dropdown;
            break;
        case "documento":
            SelectedIcon =Documento;
            break;
        case "dermatologia":
            SelectedIcon =Dermatologia;
            break;
        case "configuracion":
            SelectedIcon =Configuracion;
            break;
        case "comentar":
            SelectedIcon =Comentar;
            break;
        case "buscar":
            SelectedIcon =Buscar;
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
