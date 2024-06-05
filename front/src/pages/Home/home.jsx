import styles from "./Home.module.scss";
import {Footer} from "../../components/Footer/Footer";
import {SideBar} from "../../components/Sidebar/Sidebar";
import {Carousel} from "../../components/Carousel/Carousel";

export const Home = (props) => {
    return (
            <main className={styles.main}>
                <section className={styles.sidebar}>
                <SideBar />
                </section>
                <section className={styles.carousel}>
                <Carousel />
                </section>
                <section className={styles.footer}>
                <Footer />
                </section>
            </main>
    );
};
