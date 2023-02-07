const computer = document.getElementById("computer-choice");
const player = document.getElementById("user-choice");
const resultDisplay = document.getElementById("result");
const possilbleChoices = document.querySelectorAll("button");
let userChoice;
let computerChoice;
let result;

possilbleChoices.forEach((possilbleChoice) =>
  possilbleChoice.addEventListener("click", (e) => {
    userChoice = e.target.id;
    player.innerHTML = userChoice;

    generateComputerChoice();
    getResult();
  })
);

function generateComputerChoice() {
  const randomNumber = Math.floor(Math.random() * possilbleChoices.length);

  if (randomNumber === 0) {
    computerChoice = "rock";
  }

  if (randomNumber === 1) {
    computerChoice = "paper";
  }

  if (randomNumber === 2) {
    computerChoice = "scissors";
  }

  computer.innerHTML = computerChoice;
}

function getResult() {
  if (computerChoice === userChoice) {
    result = "It's a Draw !";
  }

  if (computerChoice === "rock" && userChoice === "paper") {
    result = "You Win !";
  }

  if (computerChoice === "paper" && userChoice === "rock") {
    result = "You Lose !";
  }

  if (computerChoice === "scissors" && userChoice === "paper") {
    result = "You Lose !";
  }

  if (computerChoice === "paper" && userChoice === "scissors") {
    result = "You Win !";
  }

  if (computerChoice === "rock" && userChoice === "scissors") {
    result = "You Lose !";
  }

  if (computerChoice === "scissors" && userChoice === "rock") {
    result = "You Win !";
  }

  resultDisplay.innerHTML = result;
}
