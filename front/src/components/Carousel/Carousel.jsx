import styles from "./Carousel.module.scss";
export  const Carousel = (props)=>{
    const images = props.images || [];
    return (
        <section className={styles.carousel}>
            <p className={styles.title}>Lorem ipsum dolor sit amet consectetur. Morbi turpis scelerisque maecenas tortor.Lorem ipsum dolor sit amet consectetur. Morbi turpis scelerisque maecenas tortor.</p>
            <div className={styles.carousel_track_container}>
                <ul
                    className={styles.carousel_track}
                >
                    {
                        images.map((image, index) => {
                            return (
                                <li key={index} className={styles.carousel_slide}>
                                    <img src={image} alt={`Imagen ${index + 1}`} />
                                </li>
                            );
                        })
                    }

                </ul>
            </div>
            <div className={styles.container_btn}>
            <button onClick={console.log('imagen 1')} className={styles.btn}></button>
            <button onClick={console.log('imagen 2')} className={styles.btn}></button>
            <button onClick={console.log('imagen 3')} className={styles.btn}></button>
            <button onClick={console.log('imagen 4')} className={styles.btn}></button>
            <button onClick={console.log('imagen 5')} className={styles.btn}></button>
            <button onClick={console.log('imagen 6')} className={styles.btn}></button>
            </div>
            <p className={styles.title}>Lorem ipsum dolor sit amet consectetur. Morbi turpis scelerisque maecenas tortor.Lorem ipsum dolor sit amet consectetur. Morbi turpis scelerisque maecenas tortor.</p>
        </section>
        
    );


};