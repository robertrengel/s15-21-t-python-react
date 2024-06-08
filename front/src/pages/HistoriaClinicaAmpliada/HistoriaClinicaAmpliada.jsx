import styles from "./HistoriaClinicaAmpliada.module.scss";
import {Input} from "../../components/Input/Input";
import {Button} from "../../components/Button/Button";
import {Icons} from "../../components/Icons/Icons";
import {ModalForm } from "../../components/ModalForm/ModalForm";
import {FileUpload} from "../../components/FileUpload/FileUpload";
import {useState} from "react";

export const HistoriaClinicaAmpliada= ()=>{

    const [isModalOpen, setIsModalOpen] = useState(false);
    const [formData, setFormData] = useState({});

    const openModal = () => {
      setIsModalOpen(true);
    };
  
    const closeModal = () => {
      setIsModalOpen(false);
    };

    const handleChange = (event) => {
        setFormData({
            ...formData,
            [event.target.name]:event.target.value
        })
        
      };

    const handleSubmit = (event) => {
        event.preventDefault(); 
        console.log('datos optenidos del formulario:', formData);
  };

      
return (
    <section className={styles.section}>
            <form  onSubmit={handleSubmit}  className={styles.form}>
                <div className={styles.form_title}>
                    <h3>Diagnostico</h3>
                </div>
                <div className={styles.container_fields}>
                    <div className={styles.group}>
                        <Input 
                            type="text" 
                            label="Nombre"
                            name="Nombre"
                            placeholder="Nombre" 
                            value={formData.name}
                            onChange={handleChange}
                        />
                        <Input 
                            type="text" 
                            label="Apellido" 
                            placeholder="Apellido" 
                            name="Apellido"
                            value={formData.name}
                            onChange={handleChange}
                        />
                    </div>
                    <div className={styles.group}>
                        <Input 
                            type="date" 
                            label="Fecha de Consulta" 
                            placeholder="Edad" 
                            name="Edad"
                            value={formData.name}
                            onChange={handleChange}
                        />
                    </div>
                        <Input 
                        type="textarea" 
                        label="Diagnostico" 
                        placeholder="input" 
                        name="Diagnostico"
                        onChange={handleChange}
                        />
                        <Input 
                            type="textarea" 
                            label="Tratamiento" 
                            placeholder="input"
                            onChange={handleChange}
                        />
                        <Input 
                            type="textarea" 
                            label="Comentarios" 
                            placeholder="input"
                            onChange={handleChange} 
                        />
                    <div className={styles.btn_carga}>
                        <div className={styles.fileUpload} >
                        <FileUpload 
                            icon={
                                <Icons 
                                    icon="documento" 
                                    size={36} 
                                    color="green"  
                                />} 
                            size={60}
                            
                        />
                        </div>
                        <div className={`${styles.modal} ${isModalOpen ? styles.modal_open : ''}`}>
                            <Button 
                                onClick={openModal}
                                width={60} 
                                height={60}
                            >
                                <Icons
                                    icon="comentar"
                                    size={33}  
                                />
                            </Button>
                            {isModalOpen && (
                                <ModalForm 
                                    title="Comentario" 
                                    onClose={closeModal}
                                >
                                    <Input
                                        type="textarea"
                                        name="Comentario"
                                    />
                                </ModalForm>
                            )}
                        </div>
                    </div>
                    <div className={styles.btn_submit}>
                            <Button   
                                width={159} 
                                height={48} 
                                onClick={()=>{console.log("boton")}}>
                                Volver
                            </Button>
                            <Button   
                                width={159} 
                                height={48} 
                                onClick={()=>{console.log("boton")}}>
                                Guardar
                            </Button>
                        </div>

                </div>
            </form>
        <article className={styles.article}>
        <div className={styles.article_title}>
            <h3>Historial</h3>
        </div>
        <div className={styles.article_cometario}>
            <time dateTime="2023-06-06" >25/05/2024</time>
            <p>
                Marcelo Perez ha agregado un nuevo documento
            </p> 
        </div>
        <div className={styles.article_cometario}>
            <time dateTime="2023-06-06" >25/05/2024</time>
            <p>
                Marcelo Perez ha agregado un nuevo documento
            </p> 
        </div>


        </article>
    </section>
)


}