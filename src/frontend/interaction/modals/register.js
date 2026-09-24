const btnReg = document.getElementById("btn-sign-up");
const freeRegBtn = document.getElementById("get-started-free");
const regModal = document.getElementById("i-signup-modal");
const closeRegModal = document.getElementById("close-register-modal");

function openModal(evt) {
    regModal.style.display = "flex";
    document.getElementsByTagName("header")[0].inert = true;
    document.getElementsByTagName("main")[0].inert = true;
}

btnReg.addEventListener("click", openModal);
freeRegBtn.addEventListener("click", openModal);

closeRegModal.addEventListener("click", evt => {
    regModal.style.display = "none";
    document.getElementsByTagName("header")[0].inert = false;
    document.getElementsByTagName("main")[0].inert = false;
});