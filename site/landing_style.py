"""Stylesheet for the generated landing page and the 404 page.

Light and calm: a white page under a soft sky-blue hero band, navy text, one
system sans stack, flat rounded buttons and white cards with hairline borders.
The game shows only in the colours: the sky blue and gold of the HUD, and a
thin strip of the wordmark's letter colours under the top bar. No images and
no web fonts (the Content-Security-Policy allows neither before launch).
"""

CSS = """
  :root {
    --bg: #f6f9fd;
    --surface: #ffffff;
    --surface-soft: #eef5fc;
    --sky: #dcefff;
    --sky-strong: #9fd3ff;
    --ink: #142038;
    --ink-dim: #4a5874;
    --ink-faint: #7a879f;
    --accent: #1f6fd6;
    --accent-hover: #1858ad;
    --gold: #f2b324;
    --line: #dde6f1;
    --line-strong: #c6d3e4;
    --shadow: 0 1px 2px rgba(20, 32, 56, 0.06), 0 12px 32px -18px rgba(20, 32, 56, 0.28);
    --font: "Segoe UI Variable Text", "Segoe UI", ui-sans-serif, Inter, Roboto, "Helvetica Neue", Arial, sans-serif;
    --font-display: "Segoe UI Variable Display", "Segoe UI", ui-sans-serif, Inter, Roboto, "Helvetica Neue", Arial, sans-serif;
    --radius: 14px;
    color-scheme: light;
  }

  * { box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body {
    margin: 0;
    background: var(--bg);
    color: var(--ink);
    font-family: var(--font);
    font-size: 17px;
    line-height: 1.6;
    text-align: center;
    -webkit-font-smoothing: antialiased;
  }
  ::selection { background: var(--sky-strong); color: var(--ink); }
  img { max-width: 100%; display: block; }
  a { color: var(--accent); text-decoration: none; }
  a:hover { color: var(--accent-hover); }
  a:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; border-radius: 6px; }
  h1, h2, h3 { margin: 0; font-family: var(--font-display); font-weight: 700; letter-spacing: -0.02em; text-wrap: balance; }

  .wrap {
    width: min(1040px, 100%);
    margin: 0 auto;
    padding: 0 clamp(1rem, 5vw, 2.4rem);
  }

  /* ---------- nav ---------- */
  .topbar {
    position: sticky;
    top: 0;
    z-index: 30;
    background: rgba(255, 255, 255, 0.9);
    border-bottom: 1px solid var(--line);
    backdrop-filter: blur(12px) saturate(140%);
  }
  .topbar::after {
    content: "";
    position: absolute;
    left: 0;
    right: 0;
    bottom: -1px;
    height: 3px;
    background: linear-gradient(90deg,
      #3b86f0 0 16.6%, #1fb3a6 16.6% 33.3%, #3fbf63 33.3% 50%,
      #f2b324 50% 66.6%, #e8384f 66.6% 83.3%, #8b4fd8 83.3% 100%);
  }
  .topbar-inner {
    width: min(1040px, 100%);
    margin: 0 auto;
    padding: 0.7rem clamp(1rem, 5vw, 2.4rem);
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    align-items: center;
    gap: 1rem;
  }
  .topbar-brand {
    justify-self: start;
    font-family: var(--font-display);
    font-weight: 700;
    font-size: 1rem;
    color: var(--ink);
  }
  .topbar-brand:hover { color: var(--ink); }
  .topbar-nav { display: flex; gap: 1.6rem; font-size: 0.92rem; font-weight: 500; }
  .topbar-nav a { color: var(--ink-dim); }
  .topbar-nav a:hover { color: var(--ink); }
  .topbar-cta { justify-self: end; }

  /* ---------- buttons ---------- */
  .btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    font-family: inherit;
    font-size: 0.95rem;
    font-weight: 600;
    padding: 0.72rem 1.45rem;
    border-radius: 10px;
    border: 1px solid transparent;
    background: var(--accent);
    color: #ffffff;
    box-shadow: 0 1px 2px rgba(20, 32, 56, 0.12), 0 8px 20px -12px rgba(31, 111, 214, 0.7);
    transition: background 0.15s ease, transform 0.15s ease;
  }
  .btn:hover { background: var(--accent-hover); color: #ffffff; transform: translateY(-1px); }
  .btn.sm { padding: 0.46rem 1rem; font-size: 0.86rem; border-radius: 8px; }
  .btn.ghost {
    background: var(--surface);
    color: var(--ink);
    border-color: var(--line-strong);
    box-shadow: 0 1px 2px rgba(20, 32, 56, 0.06);
  }
  .btn.ghost:hover { background: var(--surface-soft); color: var(--ink); border-color: var(--ink-faint); }
  .btn.soon, .btn.soon:hover {
    cursor: default;
    transform: none;
    background: var(--surface);
    color: var(--ink);
    border-color: var(--gold);
    box-shadow: inset 0 0 0 1px var(--gold);
  }

  /* ---------- hero ---------- */
  .hero {
    position: relative;
    isolation: isolate;
    overflow: hidden;
    padding: clamp(4rem, 11vw, 7rem) 0 clamp(3.4rem, 8vw, 5rem);
    background: linear-gradient(180deg, var(--sky) 0%, #eef7ff 60%, var(--bg) 100%);
  }
  .kicker {
    display: inline-block;
    font-size: 0.74rem;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 1rem;
  }
  a.studio-link:hover { color: var(--accent-hover); }
  .hero h1 {
    font-size: clamp(2.6rem, 8vw, 4.4rem);
    line-height: 1.04;
    margin-bottom: 1.1rem;
  }
  .lede {
    color: var(--ink-dim);
    font-size: clamp(1.02rem, 2.3vw, 1.16rem);
    max-width: 58ch;
    margin: 0 auto 1.9rem;
  }
  .hero-actions {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-bottom: 1.6rem;
  }
  .chips { display: flex; justify-content: center; flex-wrap: wrap; gap: 0.4rem; }
  .chip {
    font-size: 0.78rem;
    font-weight: 600;
    padding: 0.26rem 0.75rem;
    border-radius: 999px;
    border: 1px solid var(--line-strong);
    background: rgba(255, 255, 255, 0.75);
    color: var(--ink-dim);
  }
  .chip.free { color: var(--accent); border-color: var(--sky-strong); }
  .hero-art {
    display: block;
    width: min(760px, 100%);
    margin: clamp(2rem, 6vw, 3rem) auto 0;
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid var(--line);
    box-shadow: var(--shadow);
  }

  /* ---------- sections ---------- */
  section.block { padding: clamp(2.4rem, 7vw, 4rem) 0; }
  .panel {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: clamp(1.8rem, 5vw, 2.8rem) clamp(1.2rem, 4vw, 2.6rem);
    box-shadow: var(--shadow);
  }
  .block-head { margin-bottom: clamp(1.4rem, 4vw, 2rem); }
  .block-head .kicker { margin-bottom: 0.6rem; }
  .block-head h2 { font-size: clamp(1.55rem, 4vw, 2.1rem); }
  .block-dek { color: var(--ink-dim); font-size: 1rem; max-width: 58ch; margin: 0.6rem auto 0; }
  .block-more { margin-top: clamp(1.6rem, 4vw, 2.2rem); }

  /* ---------- news ---------- */
  .news-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; }
  .news-card {
    display: flex;
    flex-direction: column;
    gap: 0.55rem;
    text-align: left;
    padding: 1.3rem 1.4rem;
    border-radius: var(--radius);
    border: 1px solid var(--line);
    background: var(--surface-soft);
    color: inherit;
    transition: border-color 0.15s ease, transform 0.15s ease;
  }
  .news-card:hover { color: inherit; border-color: var(--sky-strong); transform: translateY(-2px); }
  .news-meta { display: flex; gap: 0.55rem; flex-wrap: wrap; font-size: 0.76rem; font-weight: 600; color: var(--ink-faint); }
  .news-card h3 { font-size: 1.05rem; line-height: 1.32; }
  .news-card p { margin: 0; font-size: 0.92rem; color: var(--ink-dim); }
  .news-card .more { margin-top: auto; font-size: 0.86rem; font-weight: 600; color: var(--accent); }

  /* ---------- media ---------- */
  .media-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.85rem; }
  .shot {
    position: relative;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--line);
    background: var(--surface-soft);
    transition: transform 0.15s ease, border-color 0.15s ease;
  }
  .shot:hover { transform: translateY(-2px); border-color: var(--sky-strong); }
  .shot img { aspect-ratio: 16 / 9; object-fit: cover; }
  .shot.trailer { grid-column: span 2; }
  .shot.trailer::after {
    content: "▶";
    position: absolute;
    inset: 0;
    display: grid;
    place-items: center;
    font-size: 2.2rem;
    color: #ffffff;
    text-shadow: 0 3px 14px rgba(20, 32, 56, 0.5);
    background: linear-gradient(180deg, rgba(20, 32, 56, 0.04), rgba(20, 32, 56, 0.32));
  }

  /* ---------- legal + footer ---------- */
  .legal-row { display: flex; justify-content: center; flex-wrap: wrap; gap: 0.75rem; }
  footer.site {
    padding: 2rem 0 3rem;
    color: var(--ink-faint);
    font-size: 0.86rem;
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
  }
  footer.site a { color: var(--ink-dim); }
  footer.site a:hover { color: var(--ink); }

  @media (max-width: 860px) {
    .topbar-inner { grid-template-columns: 1fr auto; }
    .topbar-nav { display: none; }
    .shot.trailer { grid-column: span 1; }
  }
  @media (prefers-reduced-motion: reduce) {
    html { scroll-behavior: auto; }
    .btn, .news-card, .shot { transition: none; }
  }
"""
