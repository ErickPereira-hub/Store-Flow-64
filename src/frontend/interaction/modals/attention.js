const basic = document.getElementById("i-basic");
const std = document.getElementById("i-std");
const premium = document.getElementById("i-premium");
const gotItBtn = document.getElementById("i-got-it")

function openModal(evt) {
    document.getElementById("i-attention-modal").style.display = "flex";
}

basic.addEventListener("click", openModal);
std.addEventListener("click", openModal);
premium.addEventListener("click", openModal);

gotItBtn.addEventListener("click", evt => {
    document.getElementById("i-attention-modal").style.display = "none";
});