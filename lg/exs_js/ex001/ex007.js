function verificarParOuImpar(numero){
    if(numero % 2 == 0){
        return `Par`
    }
    else{
        return `Ìmpar`
    }
}

console.log(verificarParOuImpar(5));