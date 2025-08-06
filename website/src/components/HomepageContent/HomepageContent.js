import gif from '@site/static/animations/homepage-gif.gif';
import logo from '@site/static/img/catlogo.png';
import hdivider from '@site/static/img/horizontal-divider.png';

import styles from './styles.module.css';

export default function HomepageContent() {
  return (<>
        <img className={styles.horizontaldivider} src={hdivider} />
        <div className={styles.container}>
            <b className={styles.poweredby}>Powered <br /> by PURL</b>
            <div className={styles.gifcontainer}>
                <img className={styles.homepagegif} src={gif} alt='Homepage GIF'/>
            </div>
            <img className={styles.logo} src={logo} alt="Purl Logo" />
        </div> </>
    );
}