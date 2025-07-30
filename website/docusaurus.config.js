// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'PURL Specs',
  tagline: 'PURL SPEC TAGLINE',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://your-docusaurus-site.example.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'Package URL', // Usually your GitHub org/user name.
  projectName: 'Perl specs', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/package-url',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/package-url',
          // Useful options to enforce blogging best practices
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'PURL',
        logo: {
          alt: 'My Site Logo',
          src: 'img/logo.png',
        },
        style: 'dark',
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'mySidebar',
            position: 'left',
            label: 'Docs',
          },
          {to: '/docs/PURL_SPECIFICATION', label: 'PURL Specs', position: 'left'},
          {to: '/docs/PURL_TYPES', label: 'PURL Types', position: 'left'},
          {
            href: 'https://github.com/package-url',
            label: 'GitHub',
            position: 'right',
          },
          {
            href: 'https://cyclonedx.slack.com/archives/C06KTE3BWEB',    
            label: 'Slack',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'News and Events',
            items: [
              {
                label: 'Newsletter',
                to: 'docs/PURL_SPECIFICATION',
              },
              {
                label: 'Meetings',
                to: 'docs/PURL_SPECIFICATION',
              },
              {
                label: 'Blog',
                to: '/blog',
              },
            ],
          },
          {
            title: 'Social',
            items: [
              {
                label: 'Gitter',
                href: 'https://app.gitter.im/#/room/#package-url_Lobby:gitter.im',
              },
              {
                label: 'Slack',
                href: 'https://cyclonedx.slack.com/archives/C06KTE3BWEB',
              },
              {
                label: 'Github',
                href: 'https://github.com/package-url',
              },
            ],
          },
          {
            title: 'References',
            items: [
              {
                label: 'CycloneDX',
                href: 'https://cyclonedx.org/',
              },
              {
                label: 'SPDX',
                href: 'https://spdx.dev/',
              },
              {
                label: 'CSAF',
                href: 'https://www.csaf.io/',
              },
              {
                label: 'OpenVEX',
                href: 'https://github.com/openvex/',
              },
              {
                label: 'OSV Schema',
                href: 'https://github.com/ossf/osv-schema',
              },
            ],
          },
          {
            title: 'Standardisation',
            items: [
              {
                label: 'ECMA',
                href: 'https://ecma-international.org',
              },
              {
                label: 'ISO',
                href: 'https://www.iso.org/home.html',
              },
              {
                label: 'ECMA TC-54 PURL',
                href: 'https://tc54.org/purl/',
              },
              {
                label: 'ECMA TC-54 CycloneDX',
                href: 'https://tc54.org/cyclonedx/',
              },
              {
                label: 'ECMA TC-54 Transparency Exchange API',
                href: 'https://tc54.org/tea/',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} PURL, Inc. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
