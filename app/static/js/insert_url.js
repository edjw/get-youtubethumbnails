"use strict";
document.getElementById("example_link").addEventListener("click", fillForm);

function fillForm() {
    let link = document.getElementById("example_link").innerText
    document.getElementById("url_submit").value = link;
}