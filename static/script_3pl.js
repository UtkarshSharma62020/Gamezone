let currentPlayer = 'X';
let gameStatus = ['', '', '', '', '', '', '', '', ''];
let aiMode = false;

function handleClick(index) {
    if (gameStatus[index] === '' && !checkWin() && !checkDraw()) {
        gameStatus[index] = currentPlayer;
        renderCell(index, currentPlayer); // Render the clicked cell immediately
        if (checkWin()) {
            renderPrompt(`${currentPlayer} wins!`);
            setTimeout(() => {
                removePrompt();
                
            }, 5000); // Remove prompt after 5 seconds and reset the game
        } else if (checkDraw()) {
            renderPrompt('It\'s a draw!');
            setTimeout(() => {
                removePrompt();
                
            }, 5000); // Remove prompt after 5 seconds and reset the game
        } else {
            if (aiMode) {
                togglePlayer();
                setTimeout(aiMove, 500); // Delay AI move for better visual effect
            } else {
                togglePlayer();
            }
        }
    }
}

function renderPrompt(message) {
    const promptElement = document.getElementById('prompt');
    promptElement.textContent = message;
}
function removePrompt() {
    const promptElement = document.getElementById('prompt');
    promptElement.textContent = ''; // Clear the prompt message
}

function togglePlayer() {
    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
}

function checkWin() {
    const winConditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
        [0, 4, 8], [2, 4, 6] // Diagonals
    ];

    for (let condition of winConditions) {
        const [a, b, c] = condition;
        if (gameStatus[a] && gameStatus[a] === gameStatus[b] && gameStatus[a] === gameStatus[c]) {
            return true;
        }
    }
    return false;
}

function checkDraw() {
    return !gameStatus.includes('');
}

function resetGame() {
    currentPlayer = 'X';
    gameStatus = ['', '', '', '', '', '', '', '', ''];
    render();
}

function render() {
    const cells = document.querySelectorAll('.cell');
    cells.forEach((cell, index) => {
        cell.textContent = gameStatus[index];
    });
}

function renderCell(index, player) {
    const cell = document.querySelector(`.cell:nth-child(${index + 1})`);
    cell.textContent = player;
}

function aiMove() {
    if (!checkWin() && !checkDraw()) {
        let bestScore = -Infinity;
        let bestMove;
        for (let i = 0; i < gameStatus.length; i++) {
            if (gameStatus[i] === '') {
                gameStatus[i] = currentPlayer; // Simulate AI move
                let score = minimax(0, false);
                gameStatus[i] = ''; // Reset the simulated move
                if (score > bestScore) {
                    bestScore = score;
                    bestMove = i;
                }
            }
        }
        gameStatus[bestMove] = currentPlayer; // Apply the AI move
        renderCell(bestMove, currentPlayer); // Render the AI move
        if (checkWin()) {
            setTimeout(() => {
                alert(`${currentPlayer} wins!`);
                resetGame();
            }, 100);
        } else if (checkDraw()) {
            setTimeout(() => {
                alert('It\'s a draw!');
                resetGame();
            }, 100);
        } else {
            togglePlayer(); // Toggle player after AI move
        }
    }
}

function minimax(depth, maximizingPlayer) {
    if (checkWin()) {
        if (currentPlayer === 'X') {
            return 10 - depth;
        } else {
            return depth - 10;
        }
    } else if (checkDraw()) {
        return 0;
    }

    if (depth >= 3) {
        return 0; // Limiting the depth of search to improve performance
    }

    if (maximizingPlayer) {
        let bestScore = -Infinity;
        for (let i = 0; i < gameStatus.length; i++) {
            if (gameStatus[i] === '') {
                gameStatus[i] = currentPlayer;
                let score = minimax(depth + 1, false);
                gameStatus[i] = '';
                bestScore = Math.max(score, bestScore);
            }
        }
        return bestScore;
    } else {
        let bestScore = Infinity;
        for (let i = 0; i < gameStatus.length; i++) {
            if (gameStatus[i] === '') {
                gameStatus[i] = currentPlayer === 'X' ? 'O' : 'X';
                let score = minimax(depth + 1, true);
                gameStatus[i] = '';
                bestScore = Math.min(score, bestScore);
            }
        }
        return bestScore;
    }
}

// Add event listeners to each cell
const cells = document.querySelectorAll('.cell');
cells.forEach((cell, index) => {
    cell.addEventListener('click', () => handleClick(index));
});

// Add event listener to the "Play with AI" button
const aiButton = document.getElementById('ai-button');
aiButton.addEventListener('click', () => {
    aiMode = true;
    resetGame();
});

// Add event listener to the "Play with 2 Players" button
const twoPlayersButton = document.getElementById('two-players-button');
twoPlayersButton.addEventListener('click', () => {
    aiMode = false;
    resetGame();
});

// Reset game on button click
const resetButton = document.querySelector('button');
resetButton.addEventListener('click', resetGame);

// Initialize game
render();