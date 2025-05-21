const vendas = [
    {produto: "Maça", quantidade: 10, precoUnitario: 0.50},
    {produto: "Banana", quantidade: 20, precoUnitario: 0.60},
    {produto: "Pera", quantidade: 30, precoUnitario: 0.80},
];

const Total = vendas.reduce((cont, i) =>{
    return cont + (i.quantidade * i.precoUnitario);
},0);

console.log(Total);