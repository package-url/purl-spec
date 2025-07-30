import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Simple and Standardized',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        PackageURL is built to be straightforward and universally understandable,
        making software package identification seamless across ecosystems.
      </>
    ),
  },
  {
    title: 'Focus on Clarity',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        With PackageURL, you can concentrate on managing your software supply chain.
        It provides a clean, consistent format for referencing packages—no more guesswork.
      </>
    ),
  },
  {
    title: 'Ecosystem-Agnostic',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        Whether you're working with npm, Maven, PyPI, or Docker, PackageURL adapts to your environment.
        It's designed to work across languages and platforms effortlessly.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
