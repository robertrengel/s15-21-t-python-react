import styles from "./Errors.module.scss";
import { Button } from "../Button/Button";


export const Errors=({name,image,description="Esta dirección ha sido escrita de manera errónea o la página se ha eliminado", ...props})=>{
   return(
           <section className={styles.error_section}>
               <div className= {styles.error_container}>
                   <div className= {styles.error_header}>
                       <h1 className= {styles.error_title}>Error</h1>
                       <h2 className= {styles.error_name}>{name}</h2>
                   </div>
                   <img className= {styles.error_image} src={image} alt={`Imagen de error ${name}`} />
               </div>
               <div className= {styles.error_description}>
                   <h3 className={styles.error_text}>{description}</h3>
                   <Button width={341} height={48} >
                       {"Volver al Inicio"}
                   </Button>
               </div>
           </section>
   );
};