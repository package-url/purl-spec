import gif from '@site/static/animations/homepage-gif.gif';
import logo from '@site/static/img/catlogo.png';
import hdivider from '@site/static/img/horizontal-divider.png';

import styles from './styles.module.css';

export default function HomepageContent() {
  return (<>
        {/* <div className={styles.horizontaldivider}> </div> */}
        <div className={styles.horizontaldivider}></div>
        <div className={styles.container}>
            <b className={styles.poweredby}>POWERED BY PURL</b>
            <div className={styles.gifcontainer}>
                <img className={styles.homepagegif} src={gif} alt='Homepage GIF'/>
            </div>
            <img className={styles.logo} src={logo} alt="Purl Logo" />
        </div> </>
    );
}