const symbols = ['😀', '😊', '😎', '😍', '🥰', '😂'];
let cards = [...symbols, ...symbols];
let flippedCards = [];
let matchedCards = [];
let attempts = 0;

let timerInterval;  // Variável que controlará o temporizador
let time = 0;  // Variável que armazenará o tempo em segundos

// Função para embaralhar o array
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

// Função que cria as cartas
function createCard(symbol) {
    const card = document.createElement('div');
    card.classList.add('card');
    card.addEventListener('click', flipCard);
    
    const cardInner = document.createElement('div');
    cardInner.classList.add('card-inner');
    
    const cardFront = document.createElement('div');
    cardFront.classList.add('card-front');
    cardFront.innerHTML = '<span>' + symbol + '</span>';
    
    const cardBack = document.createElement('div');
    cardBack.classList.add('card-back');
    
    cardInner.appendChild(cardFront);
    cardInner.appendChild(cardBack);
    card.appendChild(cardInner);
    
    return card;
}

// Função para virar a carta
function flipCard() {
    if (!flippedCards.includes(this) && !matchedCards.includes(this)) {
        this.classList.add('flipped');
        flippedCards.push(this);
        if (flippedCards.length === 2) {
            setTimeout(checkMatch, 600);
            attempts++;
            updateAttempts();
        }
    }
}

// Função que verifica se houve correspondência entre duas cartas
function checkMatch() {
    const [card1, card2] = flippedCards;
    const symbol1 = card1.querySelector('.card-front').innerText;
    const symbol2 = card2.querySelector('.card-front').innerText;

    if (symbol1 === symbol2) {
        matchedCards.push(card1, card2);
        flippedCards = [];

        if (matchedCards.length === symbols.length * 2) {
            clearInterval(timerInterval);  // Parar o temporizador quando o jogo termina
            setTimeout(() => alert('Parabéns! Você ganhou em ' + attempts + ' tentativas e ' + formatTime(time) + '!'), 500);
        }
    } else {
        flippedCards.forEach(card => card.classList.remove('flipped'));
        flippedCards = [];
    }
}

// Função que atualiza as tentativas
function updateAttempts() {
    document.getElementById('attempts').innerText = 'Tentativas: ' + attempts;
}

// Função que atualiza o tempo a cada segundo
function updateTimer() {
    time++;  // Incrementa o tempo em 1 segundo
    document.getElementById("timer").innerText = 'Tempo: ' + formatTime(time);  // Atualiza o tempo no HTML
}

// Função que formata o tempo em minutos e segundos
function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const secondsRemaining = seconds % 60;
    return `${minutes}m ${secondsRemaining < 10 ? '0' : ''}${secondsRemaining}s`;
}

// Função que reinicia o jogo
function resetGame() {
    const grid = document.getElementById('cards-grid');
    grid.innerHTML = '';
    matchedCards = [];
    attempts = 0;
    time = 0;  // Reiniciar o tempo para 0
    clearInterval(timerInterval);  // Parar o temporizador anterior
    updateAttempts();
    document.getElementById('timer').innerText = 'Tempo: 0m 00s';  // Reiniciar o contador de tempo na tela

    cards = shuffle(cards);

    cards.forEach(symbol => {
        const card = createCard(symbol);
        grid.appendChild(card);
    });

    timerInterval = setInterval(updateTimer, 1000);  // Iniciar o temporizador ao vivo
}

// Carregar o jogo quando a página é carregada
window.onload

