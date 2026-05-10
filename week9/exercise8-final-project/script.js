const taskForm = document.getElementById("taskForm");
const subjectInput = document.getElementById("subject");
const taskInput = document.getElementById("task");
const taskList = document.getElementById("taskList");
const clearTasksButton = document.getElementById("clearTasks");
const quote = document.getElementById("quote");
const quoteButton = document.getElementById("quoteButton");

const quotes = [
  "Success is the sum of small efforts repeated daily.",
  "Study hard, dream big.",
  "Discipline beats motivation.",
  "Every expert was once a beginner.",
  "Push yourself because no one else will do it for you."
];

taskForm.addEventListener("submit", function (e) {
  e.preventDefault();

  const subject = subjectInput.value.trim();
  const task = taskInput.value.trim();

  if (subject === "" || task === "") {
    quote.textContent = "Please fill both fields.";
    return;
  }

  const li = document.createElement("li");
  li.textContent = `${subject}: ${task}`;

  li.addEventListener("click", function () {
    li.remove();
  });

  taskList.appendChild(li);

  subjectInput.value = "";
  taskInput.value = "";
});

clearTasksButton.addEventListener("click", function () {
  taskList.innerHTML = "";
});

quoteButton.addEventListener("click", function () {
  const randomIndex = Math.floor(Math.random() * quotes.length);
  quote.textContent = quotes[randomIndex];
});
