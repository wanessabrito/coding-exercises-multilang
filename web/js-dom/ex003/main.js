document.addEventListener("DOMContentLoaded",function(){
    const form = document.getElementById("form");
    const nomeInput = document.getElementById("nome");
    const msg = document.getElementById("msg");

    form.addEventListener("submit", function(event){
        event.preventDefault();

        const nome = nomeInput.value.trim();

        if(nome === ""){
            msg.innerText = "Digite seu nome: ";
            msg.style.color = "red";
        }
        else{
            msg.innerText = "Formulário enviado!";
            msg.style.color = "green";
        }
    });
});