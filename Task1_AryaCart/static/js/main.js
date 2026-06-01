/* ============================================
   AryaCart — Main JavaScript
   ============================================ */

document.addEventListener('DOMContentLoaded', function () {

  /* ---------- Web Audio Sound System ---------- */
  const AudioCtx = window.AudioContext || window.webkitAudioContext;
  let _audioCtx;
  function getCtx() { 
    if (!_audioCtx) _audioCtx = new AudioCtx(); 
    if (_audioCtx.state === 'suspended') _audioCtx.resume();
    return _audioCtx; 
  }
  
  function playPopSound() {
    try {
      const ctx = getCtx();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      
      osc.type = 'sine';
      // Fast pitch sweep from high to low gives the perfect bubble pop effect
      osc.frequency.setValueAtTime(1400, ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(150, ctx.currentTime + 0.1);
      
      gain.gain.setValueAtTime(0.2, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.1);
      
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + 0.1);
    } catch (e) {}
  }

  function playClickSound() {
    try {
      const ctx = getCtx();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      
      osc.type = 'triangle';
      // Crisp subtle tactile click
      osc.frequency.setValueAtTime(900, ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(200, ctx.currentTime + 0.05);
      
      gain.gain.setValueAtTime(0.15, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.05);
      
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + 0.05);
    } catch (e) {}
  }

  function playAddCartSound() {
    try {
      const ctx = getCtx();
      // Beautiful shiny retro dual coin chime
      const osc1 = ctx.createOscillator();
      const osc2 = ctx.createOscillator();
      const gain = ctx.createGain();
      
      osc1.type = 'sine';
      osc1.frequency.setValueAtTime(987.77, ctx.currentTime); // B5
      osc1.frequency.setValueAtTime(1318.51, ctx.currentTime + 0.08); // E6
      
      osc2.type = 'triangle';
      osc2.frequency.setValueAtTime(1975.53, ctx.currentTime + 0.08); // B6
      
      gain.gain.setValueAtTime(0.12, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.35);
      
      osc1.connect(gain);
      osc2.connect(gain);
      gain.connect(ctx.destination);
      
      osc1.start();
      osc2.start();
      osc1.stop(ctx.currentTime + 0.35);
      osc2.stop(ctx.currentTime + 0.35);
    } catch (e) {}
  }

  function playSuccessSound() {
    try {
      const ctx = getCtx();
      // Upward sparkling luxury arpeggio
      const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
      notes.forEach((freq, idx) => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, ctx.currentTime + idx * 0.06);
        gain.gain.setValueAtTime(0.08, ctx.currentTime + idx * 0.06);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + idx * 0.06 + 0.2);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(ctx.currentTime + idx * 0.06);
        osc.stop(ctx.currentTime + idx * 0.06 + 0.2);
      });
    } catch (e) {}
  }

  function playErrorSound() {
    try {
      const ctx = getCtx();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(150, ctx.currentTime);
      osc.frequency.linearRampToValueAtTime(110, ctx.currentTime + 0.25);
      
      gain.gain.setValueAtTime(0.15, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.25);
      
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + 0.25);
    } catch (e) {}
  }

  /* ---------- Ripple Effect ---------- */
  document.addEventListener('click', function (e) {
    const btn = e.target.closest('.btn-gold, .btn-ripple');
    if (!btn) return;
    const rect = btn.getBoundingClientRect();
    const span = document.createElement('span');
    const size = Math.max(rect.width, rect.height);
    span.style.cssText = `width:${size}px;height:${size}px;left:${e.clientX - rect.left - size / 2}px;top:${e.clientY - rect.top - size / 2}px;`;
    span.classList.add('ripple-effect');
    btn.appendChild(span);
    setTimeout(() => span.remove(), 600);
  });

  /* ---------- Toast System ---------- */
  function getToastContainer() {
    let c = document.querySelector('.toast-container');
    if (!c) { c = document.createElement('div'); c.className = 'toast-container'; document.body.appendChild(c); }
    return c;
  }
  function showToast(message, type) {
    const t = document.createElement('div');
    t.className = 'toast toast-' + (type || 'success');
    t.innerHTML = '<span class="toast-text">' + message + '</span>';
    getToastContainer().appendChild(t);
    if (type === 'error') playErrorSound(); else playSuccessSound();
    setTimeout(() => { t.classList.add('removing'); setTimeout(() => t.remove(), 300); }, 3500);
  }
  window.showToast = showToast;

  // Convert Django messages to toasts
  document.querySelectorAll('.django-message').forEach(m => {
    const type = m.dataset.type || 'success';
    const tag = type.includes('error') ? 'error' : type.includes('warning') ? 'warning' : type.includes('info') ? 'info' : 'success';
    showToast(m.textContent.trim(), tag);
    m.remove();
  });

  /* ---------- Cart Badge Bounce ---------- */
  document.querySelectorAll('.add-to-cart-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      playAddCartSound();
      const badge = document.querySelector('.cart-badge');
      if (badge) { badge.classList.remove('bounce'); void badge.offsetWidth; badge.classList.add('bounce'); }
    });
  });

  /* ---------- Navbar Scroll Shadow ---------- */
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 30);
    });
  }

  /* ---------- Lightbox ---------- */
  function openLightbox(src) {
    playPopSound();
    const overlay = document.createElement('div');
    overlay.className = 'lightbox-overlay';
    overlay.innerHTML = '<div class="lightbox-content"><img src="' + src + '" alt="Product"><button class="lightbox-close" onclick="closeLightbox()">&times;</button></div>';
    overlay.addEventListener('click', function (e) { if (e.target === overlay) closeLightbox(); });
    document.body.appendChild(overlay);
    document.body.style.overflow = 'hidden';
  }
  function closeLightbox() {
    const o = document.querySelector('.lightbox-overlay');
    if (o) { o.remove(); document.body.style.overflow = ''; }
  }
  window.openLightbox = openLightbox;
  window.closeLightbox = closeLightbox;
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeLightbox(); });

  /* ---------- Page Transitions ---------- */
  document.querySelectorAll('a').forEach(link => {
    if (link.hostname === location.hostname && !link.hasAttribute('data-no-transition') && !link.getAttribute('href').startsWith('#')) {
      link.addEventListener('click', function (e) {
        if (e.ctrlKey || e.metaKey) return;
        e.preventDefault();
        document.body.classList.add('fade-out');
        setTimeout(() => { window.location.href = this.href; }, 200);
      });
    }
  });

  window.addEventListener('pageshow', function(event) {
    // When navigating back via bfcache, remove the fade-out class
    document.body.classList.remove('fade-out');
  });

  /* ---------- Thumbnail Click → Swap Main Image ---------- */
  document.querySelectorAll('.thumbnail-img').forEach(thumb => {
    thumb.addEventListener('click', function () {
      playPopSound();
      const main = document.querySelector('.main-product-image');
      if (main) main.src = this.dataset.src || this.src;
    });
  });

  /* ---------- Button & Link Click Sounds ---------- */
  document.addEventListener('click', function (e) {
    // Determine if the clicked element or its parent is interactive
    const interactive = e.target.closest('button, a, input[type="submit"], input[type="button"], .thumbnail');
    if (!interactive) return;
    
    // Customize sound based on type of interaction
    if (interactive.classList.contains('add-to-cart-btn')) {
      // Add-to-cart button plays its own specialized sound (already handled in specific listener, so skip)
      return;
    }
    
    if (interactive.closest('.navbar') || interactive.classList.contains('category-card') || interactive.classList.contains('thumbnail')) {
      // Pop sound for navigation, category selector, or image switcher
      playPopSound();
    } else {
      // Crisp click sound for general buttons, product links, filters
      playClickSound();
    }
  });

  /* ---------- Mobile Menu Toggle ---------- */
  const mobileBtn = document.querySelector('.mobile-menu-btn');
  const navLinksEl = document.querySelector('.nav-links');
  if (mobileBtn && navLinksEl) {
    mobileBtn.addEventListener('click', () => { navLinksEl.classList.toggle('active'); });
  }

  /* ---------- Form Submissions with sound ---------- */
  document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', () => { playPopSound(); });
  });

});
