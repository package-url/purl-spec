import gif from '@site/static/animations/homepage-gif.gif';

import styles from './styles.module.css';

export default function HomepageGif() {
  return (
        <div className={styles.container}>
            <p className={styles.label}>Examples of PURL Packages</p>
            <img className={styles.homepagegif} src={gif} alt='Homepage GIF'/>
        </div>
    );
}