let nome = "Wanessa";
let idade = 18;
let ativo = true;
let endereco = null;
let telefone; //underfined
let pessoa = {nome:"Wanessa", idade : 18}; //object 
let cores = ["azul", "verde", "roxo"];//array
let data = new Date();

let a = 5;
let b = 10;

console.log(a + b);
console.log(b < a);
console.log(a < b  && b > 7);

if (idade < 18){
    console.log("Menor de idade");
}
else if(idade === 18){
    console.log("Tem 18 anos")
}
else{
    console.log("Maior de idade")
}

for (let i = 0; i < 5; i ++){
    console.log(i + " ")
}

let i = 0;
while(i < 5){
    console.log(i + " ");
    i ++;
}

function saudacao(nome){
    return "Olá, " + nome;
}

const saudacao2 = (nome) => {
    return `Olá,` `${nome}`;
}

console.log(saudacao("Wanessa"));

const dobrar = numero => numero * 2;
 console.log(dobrar(5));
