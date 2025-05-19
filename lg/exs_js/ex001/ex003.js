function verificarNumero(numero) {
    if(numero > 0){
        return "Número positivo";
    }
    else if(numero < 0){
        return "Número negativo";
    }
    else if (numero === 0){
        return "È zero"
    }
    else{
        return "Erro"
    }
}
console.log(verificarNumero(5));