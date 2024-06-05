import styles from "./Header.module.scss"
import { Icons } from "../Icons/Icons";
  export const Header=({ name='Melania Palomino', ...props})=>{
    
    function getInitials(names) {
        return names.split(' ')
                    .map(word => word.charAt(0).toUpperCase())
                    .join('');
        
    }

    return(
        <header className={styles.header}>
            <div  className={styles.user_actions}>
                <div  className={styles.user_info}>
                    <div  className={styles.user_initials}>{getInitials(name)}
                        <div className={styles.edit_icon}>
                            <Icons icon="editar" size={24} color="#222121" />
                        </div>
                    </div>
                    <span>{name}</span>
                </div>
            </div>
            <div className={styles.search_bar} >
                <input className={styles.search} type="text" placeholder="Buscar..."/>
                <div className={styles.icon}>
                    <Icons icon="buscar" size={24} color="#222121"  />
                </div>
            </div>
            <Icons icon="configuracion" size={43.75} color="#222121" /> 

        </header>
    )
  }