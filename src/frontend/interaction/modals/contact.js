const btnContact = document.getElementById("i-contact");
const getOutFromContact = document.getElementById("i-get-out-from-contact");

function openModal(evt) {
    document.getElementById("contact-modal").style.display = "flex";
}

btnContact.addEventListener("click", openModal);

getOutFromContact.addEventListener("click", evt => {
    document.getElementById("contact-modal").style.display = "none";
});