import {fetchRegister} from "./fetch_register.js"
const form = document.getElementById("id-form-reg");
form.addEventListener("submit", evt => {
    evt.preventDefault();
    const fName = document.getElementById("id-fname-reg").value;
    const lName = document.getElementById("id-lname-reg").value;
    const email = document.getElementById("id-email-reg").value;
    const pw = document.getElementById("id-password-reg").value;
    const phone = document.getElementById("id-phone-reg").value;
    const sex = document.getElementById("id-sex-reg").value;
    const country = document.getElementById("id-country-reg").value;
    const province = document.getElementById("id-province-reg").value;
    const city = document.getElementById("id-city-reg").value;
    const bodyHTTP = {
        fname : fName,
        lname : lName,
        email : email,
        password : pw,
        phone : phone,
        sex : sex,
        country : country,
        province : province,
        city : city
    }
    fetchRegister(bodyHTTP);
});