(() => {
  'use strict';
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => Array.from(root.querySelectorAll(selector));

  // Keep the mobile navigation keyboard- and screen-reader-friendly.
  const menuButton = $('.menu-toggle');
  const nav = $('#primary-nav');
  if (menuButton && nav) {
    menuButton.addEventListener('click', () => {
      const expanded = menuButton.getAttribute('aria-expanded') === 'true';
      menuButton.setAttribute('aria-expanded', String(!expanded));
      menuButton.setAttribute('aria-label', expanded ? 'Open navigation' : 'Close navigation');
      nav.classList.toggle('is-open', !expanded);
    });
    $$('a', nav).forEach(link => link.addEventListener('click', () => {
      nav.classList.remove('is-open');
      menuButton.setAttribute('aria-expanded', 'false');
      menuButton.setAttribute('aria-label', 'Open navigation');
    }));
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape') {
        nav.classList.remove('is-open');
        menuButton.setAttribute('aria-expanded', 'false');
        menuButton.setAttribute('aria-label', 'Open navigation');
      }
    });
  }

  const workspaces = {
    aosp: {
      number: 'WORKSPACE 01', title: 'AOSP / Custom ROM',
      description: 'Select a firmware ZIP or image and carefully review the visible Fastboot partition checklist before using any flashing control.',
      controls: ['Firmware ZIP / IMG selector', 'Fastboot partition checklist', 'Auto Flash entry point', 'Fastboot and reboot controls'],
      warning: 'Potentially destructive. Confirm package, model and partition instructions first.',
      image: './screenshots/1.png', alt: 'AOSP custom ROM workspace', tab: 'tab-aosp'
    },
    hyperos: {
      number: 'WORKSPACE 02', title: 'Xiaomi HyperOS / MIUI',
      description: 'The screenshot shows ROM archive/folder or Recovery ZIP selection, three MiFlash script modes and an ARB Guard toggle.',
      controls: ['Fastboot ROM archive / folder or Recovery ZIP', 'Clean All — labelled as wiping userdata and storage', 'Save User Data — preservation is not guaranteed', 'Clean All & Lock Bootloader — dangerous with incompatible firmware'],
      warning: 'Do not relock the bootloader unless firmware and region compatibility are verified for the exact model.',
      image: './screenshots/4.png', alt: 'Xiaomi HyperOS and MIUI MiFlash workspace', tab: 'tab-hyperos'
    },
    kernel: {
      number: 'WORKSPACE 03', title: 'Kernel & Recovery',
      description: 'Choose a ZIP or IMG file and verify the intended target partition from trusted device-specific instructions.',
      controls: ['ZIP / IMG file selector', 'boot / recovery / init_boot', 'vendor_boot / dtbo partition options', 'Auto Flash and Fastboot command area'],
      warning: 'Never guess a partition based on a filename alone. Use instructions for the exact device.',
      image: './screenshots/5.png', alt: 'Kernel and recovery workspace', tab: 'tab-kernel'
    },
    console: {
      number: 'WORKSPACE 04', title: 'Terminal Console',
      description: 'Use this screen to review application-reported output and contextual device status; independently verify whether an operation succeeded.',
      controls: ['ADB / Fastboot / MiFlash-labelled output', 'Clear console control', 'Device status side panel', 'Progress ring and workflow stages'],
      warning: 'Console text is not independent proof of a successful flash. Confirm the final device state.',
      image: './screenshots/6.png', alt: 'Terminal console with application logs', tab: 'tab-console'
    },
    ram: {
      number: 'WORKSPACE 05', title: 'RAM Cleaner',
      description: 'The supplied Windows dialog shows physical RAM use, memory-area checkboxes and an Optimize Memory Now action.',
      controls: ['Physical RAM used / free display', 'Combined Page List and Modified Page List', 'Registry Cache, Standby List and System File Cache', 'Working Set and Low Priority Standby List options'],
      warning: 'Memory cleaning can be temporary and may cause caches to rebuild. Save work first; results depend on the system.',
      image: './screenshots/3.png', alt: 'Windows Memory Cleaner dialog showing memory-area checklist', tab: 'tab-ram'
    }
  };

  const panel = $('#workspace-panel');
  const panelTitle = $('#panel-title');
  const panelDescription = $('#panel-description');
  const panelCode = $('#panel-code');
  const panelControls = $('#panel-controls');
  const panelWarning = $('#panel-warning');
  const panelImage = $('#panel-image');
  const imageButton = $('#panel-image-button');
  const tabButtons = $$('[data-workspace]');

  function setWorkspace(key, shouldFocus = false) {
    const data = workspaces[key];
    if (!data || !panel) return;
    tabButtons.forEach(button => {
      const active = button.dataset.workspace === key;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-selected', String(active));
      button.tabIndex = active ? 0 : -1;
    });
    panel.setAttribute('aria-labelledby', data.tab);
    panelCode.textContent = data.number;
    panelTitle.textContent = data.title;
    panelDescription.textContent = data.description;
    panelControls.replaceChildren(...data.controls.map(text => {
      const li = document.createElement('li'); li.textContent = text; return li;
    }));
    panelWarning.querySelector('span').textContent = data.warning;
    panelImage.src = data.image;
    panelImage.alt = data.alt;
    imageButton.dataset.lightbox = data.image;
    imageButton.setAttribute('aria-label', `Open ${data.title} screenshot`);
    if (shouldFocus) panel.focus();
  }
  tabButtons.forEach(button => {
    if (!button.hasAttribute('data-workspace')) return;
    button.addEventListener('click', () => setWorkspace(button.dataset.workspace));
    button.addEventListener('keydown', event => {
      if (!['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;
      event.preventDefault();
      const current = tabButtons.filter(b => b.matches('.workspace-tab'));
      const index = current.indexOf(button);
      const next = event.key === 'Home' ? 0 : event.key === 'End' ? current.length - 1 :
        ['ArrowRight', 'ArrowDown'].includes(event.key) ? (index + 1) % current.length : (index - 1 + current.length) % current.length;
      current[next].focus();
      setWorkspace(current[next].dataset.workspace);
    });
  });
  $$('[data-workspace-link]').forEach(link => link.addEventListener('click', () => setWorkspace(link.dataset.workspaceLink)));

  const filterButtons = $$('.filter-btn');
  const galleryCards = $$('.gallery-card');
  const galleryTotal = $('#gallery-total');
  function applyFilter(filter) {
    let count = 0;
    galleryCards.forEach(card => {
      const show = filter === 'all' || card.dataset.category === filter;
      card.hidden = !show;
      if (show) count++;
    });
    filterButtons.forEach(button => {
      const active = button.dataset.filter === filter;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    if (galleryTotal) galleryTotal.textContent = `Showing ${count} screenshot${count === 1 ? '' : 's'}`;
  }
  filterButtons.forEach(button => button.addEventListener('click', () => applyFilter(button.dataset.filter)));

  const lightbox = $('#lightbox');
  const lightboxImage = $('#lightbox-image');
  const lightboxCaption = $('#lightbox-caption');
  let lastTrigger = null;
  function openLightbox(button) {
    if (!lightbox || !lightboxImage || !button.dataset.lightbox) return;
    lastTrigger = button;
    lightboxImage.src = button.dataset.lightbox;
    const sourceImage = $('img', button);
    lightboxImage.alt = sourceImage ? sourceImage.alt : button.getAttribute('aria-label') || 'Application screenshot';
    lightboxCaption.textContent = lightboxImage.alt;
    if (typeof lightbox.showModal === 'function') lightbox.showModal();
    else window.open(button.dataset.lightbox, '_blank', 'noopener,noreferrer');
  }
  $$('[data-lightbox]').forEach(button => button.addEventListener('click', () => openLightbox(button)));
  if (lightbox) {
    lightbox.addEventListener('click', event => { if (event.target === lightbox) lightbox.close(); });
    lightbox.addEventListener('close', () => { if (lastTrigger) lastTrigger.focus(); });
  }

  const year = $('#year');
  if (year) year.textContent = String(new Date().getFullYear());
})();
