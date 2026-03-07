import sys

html = """\
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>O Guia Simples dos Peptídeos</title>
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Montserrat:wght@700;800;900&display=swap" rel="stylesheet">
    <!-- AOS Animation -->
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <link rel="stylesheet" href="style.css?v=2">
</head>
<body>
    <div class="concentric-bg"></div>

    <main>
        <!-- HERO (Dark) -->
        <section class="hero-section dark-section">
            <div class="container hero-container">
                <div class="hero-left" data-aos="fade-right">
                    <h1 class="hero-title">DESCUBRA O QUE NINGUÉM TE CONTA SOBRE <span class="highlight-cyan">PEPTÍDEOS!</span></h1>
                    <p class="hero-subtitle">O guia definitivo para quem busca conhecimento, sem mitos ou termos complicados. Aprenda com rapidez e clareza.</p>
                    <ul class="hero-list">
                        <li>Sem linguagem difícil</li>
                        <li>Sem termos confusos</li>
                        <li>Sem promessas irreais</li>
                    </ul>
                    <a href="https://pay.kiwify.com.br/ZtHeS78" target="_blank" class="btn-solid">ADQUIRIR AGORA!</a>
                </div>
                <div class="hero-right" data-aos="fade-left" data-aos-delay="200">
                    <div class="book-mockup">
                        <div class="book-cover">
                            <h2 class="book-title-big">PEPTÍDEOS</h2>
                            <h3 class="book-subtitle-ref">A NOVA FRONTEIRA DA MEDICINA MOLECULAR</h3>
                        </div>
                    </div>
                </div>
            </div>
            <div class="scroll-indicator">
                <div class="mouse"></div>
            </div>
        </section>

        <!-- PROBLEM (Light) -->
        <section class="problem-section light-section">
            <div class="container dual-container">
                <div class="dual-left tall-cards" data-aos="fade-right">
                    <div class="tall-card card-cyan">
                        <span>A VERDADE</span>
                    </div>
                    <div class="tall-card card-purple">
                        <span>OS MITOS</span>
                    </div>
                </div>
                <div class="dual-right" data-aos="fade-left">
                    <h2 class="section-title text-dark">Quantas vezes você já ouviu sobre Peptídeos e encontrou apenas <span class="highlight-red">opiniões contraditórias?</span></h2>
                    <p class="section-body text-darker">
                        De um lado, há quem diga que são a solução mágica para a saúde perfeita. Do outro, há quem confunda com hormônios e trate como perigoso. No meio disso, você se pergunta:
                    </p>
                    <ul class="custom-list red-bullets">
                        <li>Quem realmente está falando a verdade?</li>
                        <li>Como separar mitos da realidade?</li>
                        <li>Quais são os mecanismos reais de ação?</li>
                    </ul>
                    <p class="section-body text-darker mt-medium">
                        A verdade é que a maioria das informações disponíveis na internet é <strong class="text-bold">superficial, técnica demais ou incompleta</strong>. E o pior: a falta de conhecimento básico impede você de entender a nova fronteira da medicina molecular.
                    </p>
                    <h3 class="sub-heading mt-large">Se você já se pegou <span class="highlight-red">pensando...</span></h3>
                    <ul class="quote-list">
                        <li>"Por que todo mundo está falando sobre Ozempic, BPC-157 e GHRP?"</li>
                        <li>"Será que isso é hormônio disfarçado?"</li>
                        <li>"Sinto que estou ficando para trás nessas novidades médicas..."</li>
                    </ul>
                    <p class="section-body text-darker mt-medium">
                        Então, você precisa ir além das informações genéricas apenas baseadas em achismos e entender <strong class="text-bold">os fundamentos dos peptídeos</strong>.
                    </p>
                </div>
            </div>
        </section>

        <!-- ACHISMO (Light) -->
        <section class="achismo-section light-section-alt">
            <div class="container dual-container reverse-mobile">
                <div class="dual-left" data-aos="fade-right">
                    <h2 class="section-title text-dark">O perigo do <span class="highlight-red">achismo</span></h2>
                    <p class="section-body text-darker mb-medium">
                        A busca por informação sem conhecimento básico pode levar a confusões sérias como:
                    </p>
                    <ul class="danger-list">
                        <li><span>1</span> Achar que todo peptídeo é anabolizante</li>
                        <li><span>2</span> Comprar falsas promessas de curas milagrosas</li>
                        <li><span>3</span> Ignorar tratamentos legítimos por medo do desconhecido</li>
                    </ul>
                </div>
                <div class="dual-right" data-aos="fade-left">
                    <p class="section-body text-darker">
                        E não se engane: <strong class="text-bold">mesmo quem acha que sabe o que está lendo pode estar cometendo erros graves de interpretação.</strong>
                    </p>
                    <p class="section-body text-darker mt-medium">
                        Mas e se você pudesse ter acesso a um conteúdo reunido em um único lugar, completo, direto e aprofundado – sem sensacionalismo científico?
                    </p>
                    <p class="section-body text-darker mt-medium">
                        É exatamente isso que <strong class="text-bold">O Guia Simples dos Peptídeos</strong> entrega. Um material abrangente, sem achismos e sem enrolação, direto ao ponto, para que você tenha o conhecimento mínimo necessário para entender o assunto.
                    </p>
                    <a href="https://pay.kiwify.com.br/ZtHeS78" target="_blank" class="btn-solid btn-red mt-large">QUERO ADQUIRIR O EBOOK!</a>
                </div>
            </div>
        </section>

        <!-- SOLUTION & ACCORDION (Dark) -->
        <section class="solution-section dark-section">
            <div class="container dual-container align-start">
                <div class="dual-left" data-aos="fade-right">
                    <h2 class="section-title">Apresentamos o <span class="highlight-cyan">Guia Simples<br>dos Peptídeos</span></h2>
                    <p class="section-body">
                        O eBook mais objetivo do mercado sobre Peptídeos! Um verdadeiro manual para quem busca entender o que são, suas características, e os reais benefícios de forma clara. Toda informação reunida em um só lugar, em linguagem 100% acessível.
                    </p>
                    <p class="section-body mt-medium">
                        Com este material, você finalmente terá um entendimento completo sobre como essas cadeias de aminoácidos conversam com as suas células, podendo tomar melhores decisões e evitar as armadilhas perigosas do "achismo".
                    </p>
                    <p class="section-highlight mt-medium cyan">O que você vai encontrar:</p>
                </div>
                <div class="dual-right" data-aos="fade-left">
                    <div class="accordion">
                        <div class="accordion-item">
                            <h3 class="accordion-header"><span>1.</span> O que são peptídeos (sem termos técnicos)</h3>
                            <div class="accordion-content">
                                <p>Explicação simples de como essas cadeias de aminoácidos atuam como mensageiros no seu corpo.</p>
                            </div>
                        </div>
                        <div class="accordion-item">
                            <h3 class="accordion-header"><span>2.</span> Por que eles não são hormônios</h3>
                            <div class="accordion-content">
                                <p>A diferença fundamental e por que as pessoas costumam confundir as duas coisas.</p>
                            </div>
                        </div>
                        <div class="accordion-item">
                            <h3 class="accordion-header"><span>3.</span> Para que vêm sendo usados hoje</h3>
                            <div class="accordion-content">
                                <p>Descubra as razões reais pelas quais ganham tanta atenção na área da saúde e estética.</p>
                            </div>
                        </div>
                        <div class="accordion-item">
                            <h3 class="accordion-header"><span>4.</span> O que é mito e o que é verdade</h3>
                            <div class="accordion-content">
                                <p>Destruindo fake news e deixando apenas a ciência traduzida.</p>
                            </div>
                        </div>
                        <div class="accordion-item">
                            <h3 class="accordion-header"><span>5.</span> Para quem esse assunto faz sentido</h3>
                            <div class="accordion-content">
                                <p>Quais os perfis que devem realmente se aprofundar nisso e se você se encaixa.</p>
                            </div>
                        </div>
                        <div class="accordion-item">
                            <h3 class="accordion-header"><span>6.</span> O que observar antes de se aprofundar</h3>
                            <div class="accordion-content">
                                <p>O guia de precauções e informações cruciais para não ser enganado.</p>
                            </div>
                        </div>
                    </div>
                    <p class="section-body text-xs mt-medium opacity-70">O Guia Simples dos Peptídeos é um manual detalhado que desvenda tudo o que você minimamente precisa saber, de forma clara, objetiva e sem sensacionalismo.</p>
                </div>
            </div>
        </section>

        <!-- WHO IS IT FOR (Dark) -->
        <section class="who-section dark-section">
            <div class="container text-center" data-aos="fade-up">
                <h2 class="section-title mb-large">Para quem é o <span class="highlight-cyan">Guia Simples dos Peptídeos?</span></h2>
                
                <div class="bento-grid columns-3">
                    <div class="bento-card center">
                        <div class="icon-box">🤔</div>
                        <h4 class="card-title">Curiosos e Interessados</h4>
                        <p class="card-body">Apenas querem entender como o corpo funciona e por que esse termo explodiu recentemente.</p>
                    </div>
                    <div class="bento-card center">
                        <div class="icon-box">🏃‍♂️</div>
                        <h4 class="card-title">Atletas e Estetas</h4>
                        <p class="card-body">Que buscam otimizar performance e saúde com base informacional de novas tendências.</p>
                    </div>
                    <div class="bento-card center">
                        <div class="icon-box">⚕️</div>
                        <h4 class="card-title">Profissionais da Saúde</h4>
                        <p class="card-body">Que precisam traduzir esse vocabulário de forma simples para seus pacientes curiosos.</p>
                    </div>
                </div>

                <div class="text-block-narrow mt-large mx-auto">
                    <p class="section-body opacity-80 mb-medium">
                        O Guia Simples não é um material qualquer. Ele foi cuidadosamente estruturado para atender diferentes perfis de leitores, desde aqueles que apenas "ouviram falar" até profissionais buscando vocabulário simplificado.
                    </p>
                    <p class="section-body opacity-80">
                        Aqui, você encontrará um conteúdo rápido e sem distorções, permitindo que tome melhores decisões, compreendendo as inovações com segurança.
                    </p>
                    <a href="https://pay.kiwify.com.br/ZtHeS78" target="_blank" class="btn-solid mt-large">ADQUIRA O LIVRO AGORA!</a>
                </div>
            </div>
        </section>

        <!-- DIFFERENT (Light) -->
        <section class="different-section light-section">
            <div class="container dual-container">
                <div class="dual-left img-center" data-aos="fade-right">
                    <div class="book-mockup scale-down">
                        <div class="book-cover">
                            <h2 class="book-title-big">PEPTÍDEOS</h2>
                            <h3 class="book-subtitle-ref">A NOVA FRONTEIRA DA MEDICINA MOLECULAR</h3>
                        </div>
                    </div>
                </div>
                <div class="dual-right" data-aos="fade-left">
                    <h2 class="section-title text-dark">O Que Torna Esse <span class="highlight-cyan">eBook Diferente?</span></h2>
                    
                    <ul class="custom-list red-bullets mt-medium">
                        <li>
                            <strong class="text-bold text-dark">Nada de achismos ou "dicas de fóruns".</strong> Aqui a informação é filtrada e entregue mastigada, com base segura.
                        </li>
                        <li>
                            <strong class="text-bold text-dark">Direto ao Ponto.</strong> Não é um tratado científico chato. A leitura flui de forma leve para que você entenda em poucas horas de leitura no celular.
                        </li>
                        <li>
                            <strong class="text-bold text-dark">Informação Neutra e Transparente.</strong> Sem hiper-promessas ou sensacionalismos de mercado. Trata das verdades cruas.
                        </li>
                        <li>
                            <strong class="text-bold text-dark">Feito para Todos os Níveis.</strong> Seja de jaleco ou calça jeans, o material tem as diretrizes para entender o tema globalmente.
                        </li>
                    </ul>
                    <a href="https://pay.kiwify.com.br/ZtHeS78" target="_blank" class="btn-solid btn-cyan mt-medium">QUERO SAIR DA DESINFORMAÇÃO!</a>
                </div>
            </div>
        </section>

        <!-- OFFER BOX (Dark) -->
        <section class="offer-section dark-section">
            <div class="container">
                <div class="offer-box" data-aos="zoom-in">
                    <div class="offer-header">
                        Adquirindo agora mesmo o <strong>Guia Simples dos Peptídeos</strong>:
                    </div>
                    <div class="offer-body">
                        <h3 class="offer-subtitle">Por apenas</h3>
                        <div class="price-display">
                            <span class="currency">R$</span>
                            <span class="amount">19,90</span>
                        </div>
                        <div class="payment-icons">
                            <img src="images/compra-segura.png" alt="Pagamento Seguro">
                        </div>
                        
                        <div class="timer-box">
                            <span class="alert-icon">⚠️</span> ESSA CONDIÇÃO É POR TEMPO LIMITADO!
                        </div>

                        <a href="https://pay.kiwify.com.br/ZtHeS78" target="_blank" class="btn-solid btn-pulse mt-medium">QUERO APROVEITAR ESTA OFERTA AGORA!</a>

                        <div class="guarantee-box mt-large">
                            <div class="guarantee-badge">7 DIAS</div>
                            <h4>Garantimos sua satisfação!</h4>
                            <p>Garantimos sua satisfação total até 7 dias da sua compra. Você achar que o Guia não é o que esperava, é só entrar em contato. Risco zero.</p>
                        </div>
                    </div>
                    
                    <div class="offer-footer">
                        <h3>Vamos recapitular?</h3>
                        <p>Você terá acesso ao material mais direto e rápido sobre Peptídeos do mercado por <strong class="highlight-cyan">apenas R$ 19,90.</strong></p>
                        <p class="font-sm opacity-80 mt-small">Não tem como não aproveitar!</p>
                        <a href="https://pay.kiwify.com.br/ZtHeS78" target="_blank" class="btn-solid btn-footer mt-medium">QUERO APROVEITAR ESTA OFERTA AGORA!</a>
                    </div>
                </div>
            </div>
            
            <!-- AVISO MEDICO (Disclaimer adicionado no redesign premium) -->
            <div class="container mt-large">
                <div class="disclaimer-card" data-aos="fade-up">
                    <div class="disclaimer-icon">⚠️</div>
                    <h3 class="disclaimer-title">Aviso de Responsabilidade e Saúde</h3>
                    <p class="disclaimer-text">Este eBook possui caráter estritamente instrucional e informativo. O conhecimento compartilhado aqui visa educar e desmistificar o tema dos peptídeos.</p>
                    <p class="disclaimer-text mt-small"><strong>Em nenhuma hipótese</strong> este material substitui uma consulta, acompanhamento clínico ou prescrição médica. Para a administração de qualquer produto ou terapia, a avaliação de um profissional de saúde qualificado é obrigatória.</p>
                </div>
            </div>
        </section>

    </main>
    
    <footer class="footer-dark">
        <div class="container text-center">
            <h2 class="footer-logo">PEPTÍDEOS</h2>
            <p class="opacity-50 font-sm">A NOVA FRONTEIRA DA MEDICINA MOLECULAR</p>
            <p class="opacity-30 font-xs mt-medium">Copyright 2026 © Todos os direitos reservados.</p>
        </div>
    </footer>

    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({ disableMutationObserver: true, once: true });
        
        // Accordion script
        document.querySelectorAll('.accordion-header').forEach(button => {
            button.addEventListener('click', () => {
                const accordionContent = button.nextElementSibling;
                button.classList.toggle('active');
                if (button.classList.contains('active')) {
                    accordionContent.style.maxHeight = accordionContent.scrollHeight + 'px';
                } else {
                    accordionContent.style.maxHeight = 0;
                }
            });
        });
    </script>
</body>
</html>
"""

with open('index.html', 'w') as f:
    f.write(html)
    
print("New index.html created successfully.")

css = """\
/* =========================================
   VARIABLES & GLOBAL
========================================= */
:root {
    --bg-dark: #0f1012;
    --bg-darker: #05050A;
    --bg-light: #f3f3f3;
    --text-white: #ffffff;
    --text-dark: #111111;
    --text-darker: #333333;
    
    /* Neons/Accents based on original + reference */
    --accent-red: #00F0FF; /* Usando Ciano onde a ref pedia vermelho */
    --accent-red-hover: #00d2df;
    --accent-cyan: #00F0FF;
    --accent-purple: #8A2BE2;
    
    --font-heading: 'Montserrat', sans-serif;
    --font-body: 'Inter', sans-serif;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html { scroll-behavior: smooth; }

body {
    font-family: var(--font-body);
    color: var(--text-white);
    background-color: var(--bg-dark);
    line-height: 1.6;
    overflow-x: hidden;
}

/* =========================================
   TYPOGRAPHY & UTILS
========================================= */
.container {
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 20px;
}

.text-center { text-align: center; }
.text-dark { color: var(--text-dark); }
.text-darker { color: var(--text-darker); }
.text-bold { font-weight: 700; }
.highlight-red { color: var(--accent-red); }
.highlight-cyan { color: var(--accent-cyan); }

.mt-small { margin-top: 10px; }
.mt-medium { margin-top: 30px; }
.mt-large { margin-top: 60px; }
.mb-medium { margin-bottom: 30px; }
.mb-large { margin-bottom: 60px; }
.mx-auto { margin-left: auto; margin-right: auto; }

.font-sm { font-size: 0.9rem; }
.font-xs { font-size: 0.75rem; }
.opacity-80 { opacity: 0.8; }
.opacity-70 { opacity: 0.7; }
.opacity-50 { opacity: 0.5; }
.opacity-30 { opacity: 0.3; }

/* SECTIONS */
.dark-section {
    background-color: var(--bg-dark);
    padding: 100px 0;
    position: relative;
    color: var(--text-white);
}

.light-section {
    background-color: #E8E8E8;
    padding: 100px 0;
    color: var(--text-dark);
}

.light-section-alt {
    background-color: #DDDDDD;
    padding: 100px 0;
    color: var(--text-dark);
}

/* =========================================
   BUTTONS
========================================= */
.btn-solid {
    display: inline-block;
    padding: 18px 40px;
    background-color: var(--accent-cyan);
    color: var(--bg-darker);
    font-family: var(--font-heading);
    font-weight: 800;
    font-size: 1rem;
    text-transform: uppercase;
    text-decoration: none;
    border-radius: 6px;
    transition: all 0.3s ease;
    box-shadow: 0 5px 20px rgba(0, 240, 255, 0.4);
    letter-spacing: 1px;
    border: none;
    cursor: pointer;
}

.btn-solid:hover {
    background-color: #fff;
    color: var(--bg-dark);
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(255, 255, 255, 0.5);
}

.btn-cyan { background-color: var(--accent-cyan); }
.btn-cyan:hover { background-color: var(--text-dark); color: #fff; }

.btn-pulse {
    animation: pulseBtn 2s infinite;
}

@keyframes pulseBtn {
    0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(0, 240, 255, 0.7); }
    70% { transform: scale(1.05); box-shadow: 0 0 0 15px rgba(0, 240, 255, 0); }
    100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(0, 240, 255, 0); }
}

.btn-footer { width: 100%; max-width: 400px; background-color: var(--accent-purple); color: #fff; box-shadow: 0 5px 20px rgba(138, 43, 226, 0.4); }
.btn-footer:hover { background-color: #fff; color: var(--accent-purple); box-shadow: 0 8px 25px rgba(255, 255, 255, 0.5); }

/* =========================================
   LAYOUT GRIDS (Reference style)
========================================= */
.dual-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
}

.align-start { align-items: flex-start; }

.section-title {
    font-family: var(--font-heading);
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 900;
    line-height: 1.1;
    margin-bottom: 25px;
    letter-spacing: -1px;
}

.section-body {
    font-size: 1.1rem;
    line-height: 1.7;
}

.sub-heading {
    font-family: var(--font-heading);
    font-size: 1.5rem;
    font-weight: 800;
    margin-bottom: 20px;
    color: var(--text-dark);
}

/* =========================================
   CONCENTRIC BACKGROUND (HERO)
========================================= */
.concentric-bg {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 900px;
    background-image: repeating-radial-gradient(
        circle at center,
        transparent,
        transparent 50px,
        rgba(255, 255, 255, 0.02) 51px,
        transparent 52px
    );
    z-index: 0;
    pointer-events: none;
}

.hero-section {
    position: relative;
    padding-top: 120px;
    min-height: 100vh;
    display: flex;
    align-items: center;
}

.hero-container {
    position: relative;
    z-index: 2;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
    align-items: center;
}

.hero-title {
    font-family: var(--font-heading);
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 900;
    line-height: 1.1;
    margin-bottom: 20px;
    text-transform: uppercase;
}

.hero-subtitle {
    font-size: 1.2rem;
    color: #ccc;
    margin-bottom: 30px;
}

.hero-list {
    list-style: none;
    margin-bottom: 40px;
}
.hero-list li {
    font-size: 1.1rem;
    margin-bottom: 10px;
    padding-left: 20px;
    position: relative;
    font-weight: 500;
}
.hero-list li::before {
    content: '•';
    color: var(--accent-cyan);
    position: absolute;
    left: 0;
    font-size: 1.5rem;
    line-height: 1;
}

/* Livro 3D */
.hero-right {
    display: flex;
    justify-content: center;
    align-items: center;
}

.book-mockup {
    position: relative;
    width: 380px;
    height: 520px;
    border-radius: 4px 15px 15px 4px;
    transform: rotateY(-20deg) rotateX(10deg);
    transform-style: preserve-3d;
    transition: transform 0.6s cubic-bezier(0.25, 1, 0.5, 1);
    box-shadow: -20px 20px 30px rgba(0, 0, 0, 0.8), 0 0 50px rgba(0, 240, 255, 0.15);
    perspective: 1200px;
    margin: 0 auto;
}
.book-mockup:hover {
    transform: rotateY(-5deg) rotateX(2deg) translateY(-10px);
}
.book-mockup::before {
    content: ''; position: absolute; top: 0; left: -34px; width: 34px; height: 100%;
    background: linear-gradient(to right, #05050A, #1a1a24);
    transform: rotateY(-90deg); transform-origin: right;
    border-radius: 4px 0 0 4px; border-left: 2px solid rgba(255,255,255,0.1);
}
.book-mockup::after {
    content: ''; position: absolute; top: 5px; right: -15px; width: 15px; height: calc(100% - 10px);
    background: #e0e0e0; transform: rotateY(90deg); transform-origin: left;
    background-image: repeating-linear-gradient(to bottom, transparent 0, transparent 2px, rgba(0,0,0,0.1) 2px, rgba(0,0,0,0.1) 4px);
}
.book-cover {
    width: 100%; height: 100%;
    background: url('/images/capa-referencia-azul.png');
    background-size: cover; background-position: center;
    border-radius: 4px 12px 12px 4px; border: 1px solid rgba(255, 255, 255, 0.08);
    position: relative; padding: 40px 15px; display: flex; flex-direction: column;
    align-items: center; text-align: center; overflow: hidden; z-index: 2;
}
.book-title-big {
    font-size: 2.8rem; font-family: 'Sora', sans-serif; color: #fff; line-height: 1.1;
    text-transform: uppercase; font-weight: 800; letter-spacing: 2px;
    text-shadow: 0 4px 10px rgba(0, 0, 0, 0.8); position: relative; z-index: 2; margin-bottom: 5px;
}
.book-subtitle-ref {
    font-size: 0.8rem; color: #4DB8FF; letter-spacing: 1px; font-family: 'Sora', sans-serif;
    font-weight: 600; text-transform: uppercase; position: relative; z-index: 2;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
}
.scale-down {
    width: 280px; height: 380px; transform: scale(0.9) rotateY(-15deg);
}

/* =========================================
   LISTS & CARDS
========================================= */
.tall-cards {
    display: flex;
    gap: 15px;
    justify-content: center;
    height: 100%;
}

.tall-card {
    width: 48%;
    border-radius: 12px;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    padding: 20px;
    color: white;
    font-family: var(--font-heading);
    font-weight: 800;
    font-size: 1.5rem;
    text-transform: uppercase;
    text-align: center;
    min-height: 400px;
    background-size: cover;
    background-position: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    position: relative;
    overflow: hidden;
}

.tall-card::after {
    content:'';
    position: absolute; bottom: 0; left: 0; width: 100%; height: 60%;
    background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
}
.tall-card span { position: relative; z-index: 2; }

.card-cyan { background-color: var(--bg-dark); border: 2px solid var(--accent-cyan); }
.card-purple { background-color: var(--bg-dark); border: 2px solid var(--accent-purple); }

.custom-list { list-style: none; margin: 20px 0; }
.custom-list li {
    font-size: 1.1rem;
    margin-bottom: 15px;
    padding-left: 25px;
    position: relative;
    color: var(--text-darker);
    font-weight: 600;
}
.custom-list li::before {
    content: '→';
    position: absolute; left: 0; color: var(--accent-cyan); font-weight: bold;
}

.quote-list { list-style: none; margin: 20px 0; border-left: 3px solid var(--accent-cyan); padding-left: 20px;}
.quote-list li { font-size: 1.1rem; font-style: italic; color: var(--text-dark); margin-bottom: 15px; }

.danger-list { list-style: none; margin-top: 30px; }
.danger-list li {
    display: flex; align-items: center; gap: 15px;
    background: #f8f8f8; padding: 15px 20px; border-radius: 8px;
    margin-bottom: 10px; font-weight: 600; font-size: 1.1rem;
    border-left: 4px solid var(--accent-cyan);
}
.danger-list li span {
    background: var(--bg-dark); color: white; width: 25px; height: 25px;
    display: flex; align-items: center; justify-content: center; border-radius: 4px; font-size: 0.9rem;
}

/* =========================================
   ACCORDION
========================================= */
.accordion { display: flex; flex-direction: column; gap: 10px; }
.accordion-item {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    overflow: hidden;
}
.accordion-header {
    background: transparent;
    color: white; padding: 20px; font-family: var(--font-heading);
    font-size: 1.1rem; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 10px;
    transition: background 0.3s;
}
.accordion-header span { color: var(--accent-cyan); }
.accordion-header:hover { background: rgba(255, 255, 255, 0.05); }
.accordion-content {
    max-height: 0; overflow: hidden; transition: max-height 0.4s ease; background: rgba(0, 0, 0, 0.2);
}
.accordion-content p { padding: 0 20px 20px 40px; color: #ccc; font-size: 0.95rem; }

/* =========================================
   CARDS GRID (PARA QUEM)
========================================= */
.bento-grid {
    display: grid; gap: 20px; width: 100%;
}
.columns-3 { grid-template-columns: repeat(3, 1fr); }

.bento-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 40px 30px; border-radius: 12px;
    transition: transform 0.3s;
}
.bento-card:hover { border-color: var(--accent-cyan); transform: translateY(-5px); }

.icon-box {
    font-size: 2.5rem; margin-bottom: 20px;
}
.card-title {
    font-family: var(--font-heading); font-size: 1.2rem; font-weight: 700; margin-bottom: 10px; color: #fff;
}
.card-body { color: #aaa; font-size: 0.95rem; }

/* =========================================
   OFFER BOX
========================================= */
.offer-box {
    max-width: 650px; margin: 0 auto;
    background: linear-gradient(135deg, #111, #1a1a24);
    border-radius: 12px; overflow: hidden;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    text-align: center;
}
.offer-header {
    background: rgba(0,240,255,0.05);
    padding: 20px; border-bottom: 1px solid rgba(255,255,255,0.05);
    font-family: var(--font-heading); font-weight: 600; color: #ccc;
}
.offer-header strong { color: var(--text-white); }
.offer-body { padding: 50px 40px; }
.offer-subtitle { font-family: var(--font-heading); font-weight: 700; font-size: 1.2rem; color: #aaa; margin-bottom: 10px; }

.price-display { display: flex; justify-content: center; align-items: flex-start; gap: 5px; color: var(--accent-cyan); margin-bottom: 20px; }
.price-display .currency { font-weight: 700; font-size: 2rem; margin-top: 10px; }
.price-display .amount { font-family: var(--font-heading); font-weight: 900; font-size: 5.5rem; line-height: 1; letter-spacing: -3px; }

.payment-icons img { height: 25px; opacity: 0.7; }
.timer-box {
    display: inline-block; background: rgba(255,255,255,0.1); padding: 8px 15px;
    border-radius: 4px; font-weight: 600; font-size: 0.85rem; letter-spacing: 1px;
    margin: 20px 0; color: #fff; border: 1px solid rgba(255,255,255,0.2);
}
.offer-footer { background: #0a0a0f; padding: 40px; border-top: 1px solid rgba(255,255,255,0.05); }

.guarantee-box { display: flex; flex-direction: column; align-items: center; gap: 15px; }
.guarantee-badge {
    background: var(--accent-purple); color: white; width: 80px; height: 80px;
    display: flex; align-items: center; justify-content: center; border-radius: 50%;
    font-family: var(--font-heading); font-weight: 900; font-size: 1.2rem; text-align: center; line-height: 1.1;
    box-shadow: 0 5px 15px rgba(138,43,226,0.4);
}
.guarantee-box h4 { font-family: var(--font-heading); font-size: 1.3rem; }
.guarantee-box p { font-size: 0.9rem; color: #999; max-width: 400px; }

/* Disclaimer */
.disclaimer-card {
    background: rgba(255, 165, 0, 0.05); border: 1px solid rgba(255, 165, 0, 0.2);
    border-radius: 12px; padding: 30px; text-align: center;
}
.disclaimer-icon { font-size: 2rem; margin-bottom: 10px; }
.disclaimer-title { font-family: var(--font-heading); color: #ffa500; margin-bottom: 15px; font-size: 1.1rem; }
.disclaimer-text { font-size: 0.85rem; color: rgba(255, 255, 255, 0.6); }

/* Footer */
.footer-dark { background: #05050a; padding: 60px 0; border-top: 1px solid rgba(255,255,255,0.05); }
.footer-logo { font-family: var(--font-heading); font-size: 2rem; font-weight: 900; letter-spacing: 3px; margin-bottom: 5px; color: #fff; }

/* =========================================
   RESPONSIVE DESIGN
========================================= */
@media (max-width: 900px) {
    .dual-container { grid-template-columns: 1fr; gap: 40px; }
    .reverse-mobile { display: flex; flex-direction: column-reverse; }
    .columns-3 { grid-template-columns: 1fr; }
    .hero-container { grid-template-columns: 1fr; text-align: center; padding-top: 50px; }
    .hero-title { font-size: 2.5rem; }
    .hero-list li { display: inline-block; padding: 0 10px; margin-bottom: 5px; }
    .hero-list li::before { display: none; }
    .book-mockup { transform: scale(0.8); }
    .tall-cards { flex-direction: column; }
    .tall-card { width: 100%; min-height: 200px; }
    .price-display .amount { font-size: 4rem; }
}
"""

with open('style.css', 'w') as f:
    f.write(css)

print("New style.css created successfully.")
