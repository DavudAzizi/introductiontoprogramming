const todoForm = document.querySelector("#todoForm");
const todoInput = document.querySelector("#todoInput");
const todoList = document.querySelector("#todoList");
const clearAll = document.querySelector("#clearAll");

let todos = JSON.parse(localStorage.getItem("todos")) || [];

function saveTodos() {
    localStorage.setItem("todos", JSON.stringify(todos));
}

function renderTodos() {
    todoList.innerHTML = "";

    todos.forEach(function (todo, index) {
        const li = document.createElement("li");
        li.textContent = todo;

        li.addEventListener("click", function () {
            todos.splice(index, 1);
            saveTodos();
            renderTodos();
        });

        todoList.appendChild(li);
    });
}

todoForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const task = todoInput.value.trim();

    if (task !== "") {
        todos.push(task);
        saveTodos();
        renderTodos();
        todoInput.value = "";
    }
});

clearAll.addEventListener("click", function () {
    todos = [];
    saveTodos();
    renderTodos();
});

renderTodos();
