const exampleSocket = new WebSocket("ws://10.2.2.2:8888");

exampleSocket.onopen = () => {
    console.log("Connection établie");
    exampleSocket.send("Je suis un client et je viens de me connecter.");

    const inputField = document.createElement("input");
    inputField.setAttribute("type", "text");
    inputField.setAttribute("placeholder", "Entrez un message...");
    document.body.appendChild(inputField);

    inputField.addEventListener("keydown", (event) => {
        if (event.key === "Enter") {
            exampleSocket.send(inputField.value);
            inputField.value = ""; 
        }
    });
};

exampleSocket.onmessage = (event) => {
    console.log("Message reçu du serveur:", event.data);
    alert("Message reçu du serveur: " + event.data);
};

exampleSocket.onerror = (error) => {
    console.error("Erreur WebSocket:", error);
};

exampleSocket.onclose = () => {
    console.log("Connection terminée");
};
