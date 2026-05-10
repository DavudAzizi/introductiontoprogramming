const taskForm = document.querySelector("#taskForm");
const subjectInput = document.querySelector("#subject");
const taskInput = document.querySelector("#task");
const taskList = document.querySelector("#taskList");
const clearTasks = document.querySelector("#clearTasks");
const quoteButton = document.querySelector("#quoteButton");
const quote = document.querySelector("#quote");

let tasks = JSON.parse(localStorage.getItem("studyTasks")) || [];

function saveTasks() {
    localStorage.setItem("studyTasks", JSON.stringify(tasks));
}

function renderTasks() {
    taskList.innerHTML = "";

    tasks.forEach(function (item, index) {
        const li = document.createElement("li");
        li.textContent = `${item.subject}: ${item.task}`;

        if (item.done) {
            li.classList.add("done");
        }

        li.addEventListener("click", function () {
            tasks[index].done = !tasks[index].done;
            saveTasks();
            renderTasks();
        });

        taskList.appendChild(li);
    });
}

taskForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const subject = subjectInput.value.trim();
    const task = taskInput.value.trim();

    if (subject === "" || task === "") {
        alert("Please fill both fields.");
        return;
    }

    tasks.push({
        subject: subject,
        task: task,
        done: false
    });

    saveTasks();
    renderTasks();

    subjectInput.value = "";
    taskInput.value = "";
});

clearTasks.addEventListener("click", function () {
    tasks = [];
    saveTasks();
    renderTasks();
});

quoteButton.addEventListener("click", function () {
    const quotes = [
        "Small steps every day lead to big results.",
        "Study now, be proud later.",
        "Discipline beats motivation.",
        "Every expert was once a beginner.",
        "Your future depends on what you do today."
    ];

    const randomIndex = Math.floor(Math.random() * quotes.length);
    quote.textContent = quotes[randomIndex];
});

renderTasks();
