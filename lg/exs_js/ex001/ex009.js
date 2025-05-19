function valorIdade(idade){
    if(idade < 18){
        return `Menor de idade`;
    }
    else if(idade >= 18){
        return `Maior de idade`;
    }
    else{
        return `Erro`;
    }
}

console.log(valorIdade(18));