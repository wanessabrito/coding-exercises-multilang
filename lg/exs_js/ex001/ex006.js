function calcularMedia(n1,n2,n3){
    let media = (n1 + n2 + n3)/3;

    if(media >= 7){
        return `Aprovado com média ${media.toFixed(1)}`
    }
    else{
        return `Reprovado com média ${media.toFixed}`
    }
}

console.log(calcularMedia(10,5,8));

