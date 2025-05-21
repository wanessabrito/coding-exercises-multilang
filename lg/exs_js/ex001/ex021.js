const temperaturas = [
    {diaSemana: "Segunda-feira", temp: 25},
    {diaSemana: "Terça-feira", temp: 17},
    {diaSemana: "Quarta-feira", temp: 32},
    {diaSemana: "Quinta-feira", temp: 19},
    {diaSemana: "Sexta-feira", temp: 24}
];

const diasQuentes = temperaturas.filter(tp => tp.temp > 30);
const diasQuentesNome = diasQuentes.map(tp => tp.diaSemana);
console.log("Dias da semana que passaram de 30°C:",diasQuentesNome.join(", "));