const produto = [
    {nome: "Celular", preco: 1500, qnt: 5},
    {nome: "Notebook", preco: 3500, qnt: 3},
    {nome: "Fone de ouvido", preco: 250, qnt: 10},
    {nome: "Monitor", preco: 1000, qnt: 4},
];

produto.forEach(produto => {
    console.log(`Produto: ${produto.nome}`);
});

produto.forEach(produto => {
    const totalProduto = produto.preco * produto.qnt;
    console.log(`O total em estoque de ${produto.nome} é R$${totalProduto}`);
});

const TotalGeral = produto.reduce((soma, produto) => {
    return soma + (produto.preco * produto.qnt);
}, 0);

console.log(`O valor total de produtos no estoque: R$${TotalGeral}`);
