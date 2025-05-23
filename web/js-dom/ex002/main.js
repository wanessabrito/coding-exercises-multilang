const cores = ["red", "blue", "green"];

cores.forEach(cor => {
    const button = document.getElementById(cor);
    button.addEventListener("click", () => {
        document.body.style.backgroundColor = cor;
    });
});