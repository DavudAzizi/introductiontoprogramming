const form = document.querySelector("#form");
const message = document.querySelector("#message");

form.addEventListener("submit", function (event) {
    event.preventDefault();

    const name = document.querySelector("#name").value.trim();
    const email = document.querySelector("#email").value.trim();
    const password = document.querySelector("#password").value.trim();

    if (name === "" || email === "" || password === "") {
        message.textContent = "All fields are required.";
        message.className = "error";
        return;
    }

    if (!email.includes("@") || !email.includes(".")) {
        message.textContent = "Please enter a valid email.";
        message.className = "error";
        return;
    }

    if (password.length < 6) {
        message.textContent = "Password must be at least 6 characters.";
        message.className = "error";
        return;
    }

    message.textContent = "Registration successful!";
    message.className = "success";
    form.reset();
});
