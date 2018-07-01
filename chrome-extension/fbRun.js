'use strict';

// chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
//     chrome.tabs.executeScript(
//         tabs[0].id,
//         // {code: 'document.body.style.backgroundColor = "' + color + '";'});
//         {code: 'alert("Hello World")'});
// });

// console.log('weird');

var m = false;
var n = false;

function send_theirs() {
    var msgs = [];
    if (!m && document.querySelector("._hh7")) {
        var incoming_msgs = document.querySelectorAll("._hh7");
        incoming_msgs.forEach(function(msg) {
            if (!msg.parentElement.classList.contains("._nd_")) // Not my own message
                msgs.push(msg.innerText);
        });
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
            // Typical action to be performed when the document is ready:
                console.log(xhttp.responseText);
            }
        };
        // console.log(msgs);
        xhttp.open("GET", "https://localhost:5000/rcv?data="+encodeURIComponent(JSON.stringify({messages: msgs})), true);
        // xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
        // xhttp.send({messages: msgs});
        xhttp.send();
        m = true;
    }
}

function send_ours() {
    var msgs = [];
    if (!n && document.querySelector("._nd_ ._hh7")) {
        var incoming_msgs = document.querySelectorAll("._nd_ ._hh7");
        incoming_msgs.forEach(function(msg) {
            msgs.push(msg.innerText);
        });
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
            // Typical action to be performed when the document is ready:
                var res = JSON.parse(xhttp.responseText);
                console.log(res);
                if (res.success)
                    alert("The messages you have been sending contain language that suggest bullying. Please refrain from the same as the receiver has the authority to take action.");
            }
        };
        // console.log(msgs);
        xhttp.open("GET", "https://localhost:5000/rcv?data="+encodeURIComponent(JSON.stringify({messages: msgs})), true);
        // xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
        // xhttp.send({messages: msgs});
        xhttp.send();
        n = true;
    }
}

window.onload = function() {
    var p = document.querySelector("#facebook ._-kb div");
    p.onkeyup = send_ours;
    p.onclick = send_theirs;
};