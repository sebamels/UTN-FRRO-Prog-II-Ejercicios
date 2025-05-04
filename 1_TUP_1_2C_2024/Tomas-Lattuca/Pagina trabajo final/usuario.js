document.addEventListener("DOMContentLoaded", () => {
    const username = localStorage.getItem("loggedInUser");
    const welcomeMessageElement = document.getElementById("welcomeMessage");

    if (username && welcomeMessageElement) {
        welcomeMessageElement.textContent = `Has iniciado sesión como ${username}`;
    }
});
