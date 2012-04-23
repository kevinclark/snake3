function print(msg) {
    var output = document.getElementById("output");
    output.innerHTML = msg;
}

var socket = new WebSocket("ws://localhost:8888/");
socket.onmessage = function (msg) {
    print(msg.data);
}
socket.onclose = function () {
    print("CLOSED");
}
    
ks = [];
document.onkeydown = function (e) {
    ks.push(e.keyCode);
}

function sendKeys () {
    socket.send(JSON.stringify(ks));
    ks = []

    window.setTimeout(sendKeys, 250);
}

window.setTimeout(sendKeys, 250);
