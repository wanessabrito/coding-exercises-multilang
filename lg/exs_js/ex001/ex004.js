let pessoa = {
    nome:"Wanessa",
    idade:18,
    cidade: "Goiânia"
};

function exibirDados(p){
    return `Olá! Meu nome é ${p.nome}, tenho ${p.idade} anos e moro em ${p.cidade}.`;
}

console.log(exibirDados(pessoa));