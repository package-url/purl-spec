import gif from '@site/static/animations/homepage-gif.gif';

import styles from './styles.module.css';

export default function HomepageGif() {
  return (<>
        <p className={styles.label}>POWERED BY PURL</p>
        <div className={styles.container}>
            <img className={styles.homepagegif} src={gif} alt='Homepage GIF'/>
        </div>
    </>);
}