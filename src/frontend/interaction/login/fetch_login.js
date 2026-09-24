export function fetchLogin(bodyHTTP) {

    const url = "http://localhost:8000/user/login";
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
        if (statusCode === 200) {
            console.log("OK");
            console.log(json);
        } else {
            document.getElementById("id-att-login").style.display = "flex";
        }
    }).catch(err => {
        console.error(err);
    });
}