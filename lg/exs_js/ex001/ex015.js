const despesas = [
    1000,150,100,900,200
];
const total = despesas.reduce((cont,i) => cont + i, 0);
console.log(total);