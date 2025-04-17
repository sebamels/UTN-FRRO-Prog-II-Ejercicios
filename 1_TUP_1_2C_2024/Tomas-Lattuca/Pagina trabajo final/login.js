function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const validUsername = "admin";
    const validPassword = "admin";

    if (username === validUsername && password === validPassword) {
        document.getElementById("loginMessage").textContent = "Datos ingresados correctamente";
        document.getElementById("loginMessage").style.color = "green";

        localStorage.setItem("loggedInUser", username);

        setTimeout(() => {
            window.location.href = "restaurantepagina.html";
        }, 2000);
    } else {
        document.getElementById("loginMessage").textContent = "Usuario o contraseña incorrectos";
        document.getElementById("loginMessage").style.color = "red";
    }
}
