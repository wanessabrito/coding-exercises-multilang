function contarVogais(palavra){
    let vogais = "aeiouAEIOU";
    let cont = 0;

    for(let i = 0; i < palavra.length; i ++){
        if(vogais.includes(palavra[i])){
            cont ++
        }
    }

    return cont
}

console.log(contarVogais("Wanessa"));