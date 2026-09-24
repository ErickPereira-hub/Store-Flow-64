const btnLogin = document.getElementById("btn-sign-in");
const loginModal = document.getElementById("login-modal");
const closeLoginModal = document.getElementById("close-login-modal");

function openModal(evt) {
    loginModal.style.display = "flex";
    document.getElementsByTagName("header")[0].inert = true;
    document.getElementsByTagName("main")[0].inert = true;
}

btnLogin.addEventListener("click", openModal);

closeLoginModal.addEventListener("click", evt => {
    loginModal.style.display = "none";
    document.getElementsByTagName("header")[0].inert = false;
    document.getElementsByTagName("main")[0].inert = false;
});