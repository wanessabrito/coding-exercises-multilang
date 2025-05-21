const produto = [
    {nome:"Banana", preco: 0.60},
    {nome:"Maça", preco: 0.50},
    {nome:"Laranja", preco: 0.30}
];

function novoPreco(){
    const precoAtualizado = produto.map(i =>{
        return{
            nome: i.nome,
            preco: (i.preco - (i.preco * 0.10)).toFixed(2)
        };
    });
    console.log(precoAtualizado);
}

novoPreco();