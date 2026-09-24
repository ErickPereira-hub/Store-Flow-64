import {fetchLogin} from "./fetch_login.js"
const form = document.getElementById("id-login");
form.addEventListener("submit", evt => {
    evt.preventDefault();
    const email = document.getElementById("id-email-login").value;
    const pw = document.getElementById("id-pw-login").value;
    const bodyHTTP = {
        email : email,
        password : pw
    }
    fetchLogin(bodyHTTP);
});