import styles from "./HistoriaClinicaAmpliada.module.scss";
import {Input} from "../../components/Input/Input";
import {Button} from "../../components/Button/Button";
import {Icons} from "../../components/Icons/Icons"
import {FileUpload} from "../../components/FileUpload/FileUpload";

export const HistoriaClinicaAmpliada= ()=>{

return (

<>
<section className={styles.section}>
        <form  action="" className={styles.form}>
            <div className={styles.form_title}>
                <h1>Diagnostico</h1>
                <hr />  
            </div>
            <div className={styles.container_fields}>
                <div className={styles.group}>
                    <Input type="text" label="Nombre" placeholder="Nombre" />
                    <Input type="text" label="Apellido" placeholder="Apellido" />
                </div>
                <div className={styles.group}>
                    <Input type="date" label="Fecha de Consulta" placeholder="Edad" />
                </div>
                    <Input type="textarea" label="Diagnostico" placeholder="input" />
                    <Input type="textarea" label="Tratamiento" placeholder="input" />
                    <Input type="textarea" label="Comentarios" placeholder="input" />
                <div className={styles.btn_carga}>
                    <FileUpload icon={<Icons icon="documento" size={36} color="green"  />} size={60} />
                    <Button onClick={()=>{console.alert("boton")}} width={60} height={60} >
                        <Icons icon="comentar" size={33}   />
                    </Button>
                </div>
                <div className={styles.btn_submit}>
                <Button   width={159} height={48} onClick={()=>{console.log("boton")}}>Volver</Button>
                <Button   width={159} height={48} onClick={()=>{console.log("boton")}}>Guardar</Button>

                </div>



            </div>
        </form>
    <article className={styles.article}>
    <div className={styles.article_title}>
        <h3>Historial</h3>
        <hr />  
    </div>
    <div className={styles.article_cometario}>
        <time datetime="2023-06-06" >25/05/2024</time>
        <p>
            Marcelo Perez ha agregado un nuevo documento
        </p> 
    </div>
    <hr />
    <div className={styles.article_cometario}>
        <time datetime="2023-06-06" >25/05/2024</time>
        <p>
            Marcelo Perez ha agregado un nuevo documento
        </p>
    </div>
    <hr />
    <div className={styles.article_cometario}>
        <time datetime="2023-06-06" >25/05/2024</time>
        <p>
            Marcelo Perez ha agregado un nuevo documento
        </p>
    </div>

    </article>
</section>

</>


)


}