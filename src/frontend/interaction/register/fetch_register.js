export function fetchRegister(bodyHTTP) {

    const url = "http://localhost:8000/user/register";
    let statusCode;
    fetch(url, {
        credentials: "include",
        method: "POST",
        body : JSON.stringify(bodyHTTP),
        headers : {"Content-Type" : "application/json"}
    }).then(res => {
        statusCode = res.status;
        return res.json();
    }).then(json => {
        if (statusCode === 201) {
            console.log("OK");
        } else {
            document.getElementById("id-att-reg").style.display = "flex";
        }
    }).catch(err => {
        console.error(err);
    });
}