import sys

with open('style.css', 'r') as f:
    lines = f.readlines()

css_top = "".join(lines[:214])

new_css = """
/* =========================================
   BENTO GRID & SHARED
========================================= */
.bento-grid {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 20px;
    width: 100%;
}

.bento-card {
    background: rgba(10, 10, 15, 0.6);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 20px;
    padding: 40px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.05);
    transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
}

.bento-card:hover {
    border-color: rgba(138, 43, 226, 0.3);
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

.flex-center {
    display: flex;
    align-items: center;
    justify-content: center;
}

.col-wide {
    grid-column: span 8;
}

.bento-visual {
    grid-column: span 4;
}

.mt-medium {
    margin-top: 20px;
}

.mb-large {
    margin-bottom: 50px;
}

.text-glow-cyan {
    text-shadow: 0 0 15px rgba(0, 240, 255, 0.6);
}

/* =========================================
   HERO SECTION
========================================= */
.hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 100px 5% 50px;
    position: relative;
}

.hero-container {
    max-width: 1200px;
    width: 100%;
    margin: 0 auto;
}

.hero-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 40px;
}

.hero-visual {
    position: relative;
    width: 280px;
    height: 380px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.glow-orb.hero-orb {
    position: absolute;
    width: 250px;
    height: 250px;
    background: var(--neon-purple);
    filter: blur(80px);
    opacity: 0.5;
    z-index: 0;
}

.book-mockup {
    position: relative;
    z-index: 1;
    width: 240px;
    height: 340px;
    background: linear-gradient(135deg, #111 0%, #05050A 100%);
    border-radius: 8px 16px 16px 8px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-left: 4px solid #222;
    box-shadow: -10px 0 20px rgba(0,0,0,0.5), inset 2px 0 5px rgba(255,255,255,0.05), 0 20px 40px rgba(0, 0, 0, 0.5);
    padding: 30px 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    overflow: hidden;
}

.book-badge {
    font-size: 0.6rem;
    color: var(--neon-cyan);
    letter-spacing: 2px;
    margin-bottom: 20px;
    font-family: var(--font-heading);
}

.book-title {
    font-size: 1.4rem;
    font-family: var(--font-heading);
    color: #fff;
    line-height: 1.2;
}

.book-art {
    margin-top: auto;
    position: relative;
    width: 100%;
    height: 100px;
}

.book-node {
    position: absolute;
    border: 2px solid var(--neon-cyan);
    border-radius: 50%;
    background: transparent;
}

.book-n1 { width: 30px; height: 30px; left: 30%; top: 10%; border-color: var(--neon-purple); }
.book-n2 { width: 15px; height: 15px; left: 70%; top: 40%; }
.book-n3 { width: 20px; height: 20px; left: 45%; top: 70%; }

.book-line {
    position: absolute;
    background: linear-gradient(to right, var(--neon-cyan), var(--neon-purple));
    height: 2px;
}

.book-l1 { width: 40px; left: 42%; top: 25%; transform: rotate(20deg); }
.book-l2 { width: 30px; left: 52%; top: 55%; transform: rotate(-40deg); }

.hero-text {
    max-width: 800px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 25px;
}

.badge {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--neon-purple);
    font-weight: 700;
    background: rgba(138, 43, 226, 0.1);
    border: 1px solid rgba(138, 43, 226, 0.3);
    padding: 8px 16px;
    border-radius: 100px;
}

.hero-title {
    font-size: clamp(2.5rem, 6vw, 4.5rem);
    letter-spacing: -0.03em;
    line-height: 1.1;
}

.hero-title span {
    background: linear-gradient(135deg, var(--text-main) 0%, var(--neon-cyan) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
}

.hero-subtitle {
    font-size: clamp(1.1rem, 2vw, 1.25rem);
    color: var(--text-muted);
    max-width: 600px;
}

/* =========================================
   PROBLEM SECTION
========================================= */
.problem-section {
    padding: 70px 0;
    position: relative;
}

.section-title {
    font-size: clamp(1.8rem, 4vw, 2.5rem);
    margin-bottom: 15px;
    line-height: 1.2;
}

.section-body {
    font-size: 1.15rem;
    color: var(--text-muted);
}

.section-highlight {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--neon-cyan);
    border-left: 2px solid var(--neon-purple);
    padding-left: 20px;
}

.glass-molecule-mini {
    position: relative;
    width: 200px;
    height: 200px;
}

.glass-molecule-mini .node {
    position: absolute;
    background: rgba(255,255,255,0.05);
    border: 2px solid var(--neon-cyan);
    border-radius: 50%;
}
.glass-molecule-mini .n-core { width: 50px; height: 50px; top: 75px; left: 75px; border-color: var(--neon-purple); box-shadow: inset 0 0 10px rgba(138,43,226,0.5); }
.glass-molecule-mini .n1 { width: 30px; height: 30px; top: 10px; left: 100px; }
.glass-molecule-mini .n2 { width: 35px; height: 35px; bottom: 20px; left: 40px; }

.glass-molecule-mini .line {
    position: absolute;
    background: linear-gradient(to right, var(--neon-cyan), var(--neon-purple));
    height: 2px;
    transform-origin: left center;
}
.glass-molecule-mini .l1 { width: 60px; top: 100px; left: 100px; transform: rotate(-70deg); }
.glass-molecule-mini .l2 { width: 70px; top: 100px; left: 100px; transform: rotate(120deg); }


/* =========================================
   SOLUTION SECTION
========================================= */
.solution-section {
    padding: 80px 0;
    position: relative;
}

.solution-card {
    position: relative;
    max-width: 900px;
    margin: 0 auto;
    overflow: hidden;
    padding: 60px 50px;
}

.soft-gradient-conic {
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% -20%, rgba(0, 240, 255, 0.1), transparent 70%);
    pointer-events: none;
}

.solution-title {
    font-size: clamp(2rem, 4vw, 3rem);
    margin-bottom: 25px;
}

.solution-text {
    font-size: clamp(1.1rem, 2vw, 1.3rem);
    color: var(--text-muted);
    line-height: 1.8;
}

.highlight.cyan {
    color: var(--neon-cyan);
    font-weight: 600;
}


/* =========================================
   LEARN SECTION (FLOW)
========================================= */
.learn-section {
    padding: 60px 0;
}

.learn-grid .step-card {
    grid-column: span 6;
    display: flex;
    flex-direction: column;
    gap: 20px;
    padding: 30px;
}

.learn-grid .col-wide {
    grid-column: span 12;
}

.step-num-bg {
    font-family: var(--font-heading);
    font-size: 2.5rem;
    font-weight: 900;
    color: transparent;
    -webkit-text-stroke: 1px rgba(255, 255, 255, 0.15);
    line-height: 1;
}

.step-card:hover .step-num-bg {
    -webkit-text-stroke: 1px var(--neon-cyan);
    text-shadow: 0 0 20px rgba(0, 240, 255, 0.2);
}

.step-text {
    font-size: 1.2rem;
    font-weight: 500;
    color: #fff;
    margin: 0;
}


/* =========================================
   DIFFERENTIAL SECTION
========================================= */
.differential-section {
    padding: 80px 0;
}

.diff-container {
    display: flex;
    gap: 60px;
    align-items: flex-start;
}

.diff-left {
    flex: 0 0 40%;
    position: sticky;
    top: 150px;
}

.sticky-title {
    font-size: clamp(2.5rem, 4vw, 3.5rem);
    line-height: 1.1;
}

.font-light.dimmed {
    font-weight: 300;
    color: rgba(255, 255, 255, 0.6);
}

.font-black.purple {
    font-weight: 800;
    color: var(--neon-purple);
}

.diff-right {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 30px;
}

.diff-card {
    padding: 35px;
}

.diff-card p {
    font-size: 1.2rem;
    margin: 0;
}


/* =========================================
   DISCLAIMER SECTION
========================================= */
.disclaimer-section {
    padding: 50px 0;
}

.disclaimer-card {
    border-color: rgba(255, 255, 255, 0.1);
    background: transparent;
    padding: 30px;
    text-align: left;
    max-width: 900px;
    margin: 0 auto;
    border-left: 3px solid rgba(255, 255, 255, 0.3);
}

.disclaimer-icon {
    font-size: 1.5rem;
    margin-bottom: 10px;
}

.disclaimer-title {
    font-size: 1.1rem;
    color: #fff;
    margin-bottom: 15px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.disclaimer-text {
    font-size: 0.95rem;
    color: var(--text-muted);
    margin-bottom: 15px;
}

.disclaimer-text:last-child {
    margin-bottom: 0;
}


/* =========================================
   OFFER SECTION
========================================= */
.offer-section {
    padding: 90px 0;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
}

.glow-orb-bg {
    position: absolute;
    width: 300px;
    height: 300px;
    background: var(--neon-purple);
    filter: blur(120px);
    opacity: 0.2;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    pointer-events: none;
    z-index: 0;
}

.offer-card {
    position: relative;
    max-width: 600px;
    width: calc(100% - 2rem);
    margin: 0 auto;
    z-index: 1;
    border-radius: 24px;
    padding: 2px;
}

.border-glow {
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, var(--neon-cyan), var(--neon-purple));
    border-radius: 24px;
    z-index: 0;
}

.offer-inner {
    position: relative;
    background: #08080C;
    border-radius: 22px;
    padding: 60px 40px;
    z-index: 1;
    text-align: center;
    border: none;
}

.offer-title {
    font-size: 1.5rem;
    color: var(--text-muted);
    margin-bottom: 20px;
    font-family: var(--font-heading);
}

.price-callout {
    margin-bottom: 30px;
    display: flex;
    align-items: flex-start;
    justify-content: center;
}

.currency {
    font-size: 2rem;
    font-weight: 700;
    margin-top: 15px;
    margin-right: 5px;
    color: var(--neon-cyan);
}

.price-value {
    font-family: var(--font-heading);
    font-weight: 900;
    font-size: clamp(3.5rem, 8vw, 6rem);
    letter-spacing: -2px;
    color: #FFF;
    text-shadow: 0px 4px 60px rgba(0, 240, 255, 0.4);
}

.offer-body {
    font-size: 1rem;
    color: var(--text-muted);
    margin-bottom: 40px;
}

.offer-btn {
    width: 100%;
}


/* =========================================
   FINAL END
========================================= */
.final-section {
    padding: 100px 5% 150px 5%;
    position: relative;
}

.final-container {
    max-width: 800px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
}

.radial-bottom-glow {
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 80vw;
    height: 50vh;
    background: radial-gradient(circle at bottom, rgba(138, 43, 226, 0.15) 0%, rgba(0, 240, 255, 0.1) 40%, rgba(5, 5, 10, 0) 70%);
    pointer-events: none;
    z-index: 0;
}

.final-title {
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 700;
    margin-bottom: 30px;
}

.final-body {
    font-size: 1.15rem;
    color: var(--text-muted);
    margin-bottom: 50px;
}

.text-bold {
    font-weight: 700;
    color: #FFF;
}

.pulse-ring {
    animation: pulseRing 3s infinite;
}

@keyframes pulseRing {
    0% {
        box-shadow: 0 0 0 0 rgba(0, 240, 255, 0.4);
    }
    70% {
        box-shadow: 0 0 0 20px rgba(138, 43, 226, 0);
    }
    100% {
        box-shadow: 0 0 0 0 rgba(0, 240, 255, 0);
    }
}


/* =========================================
   MEDIA QUERIES (MOBILE)
========================================= */
@media (max-width: 900px) {
    .bento-grid {
        display: flex;
        flex-direction: column;
    }
    
    .bento-card {
        width: 100%;
        padding: 30px 25px;
    }

    .diff-container {
        flex-direction: column;
        gap: 40px;
    }

    .diff-left {
        position: static;
    }
    
    .hero-content {
        gap: 30px;
    }
}
"""

with open('style.css', 'w') as f:
    f.write(css_top + new_css)
