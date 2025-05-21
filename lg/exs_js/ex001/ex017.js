const alunos =[
    {nome: "Wanessa", nota1: 8, nota2: 10},
    {nome: "Pedro", nota1: 10, nota2: 10},
    {nome: "Yasmim", nota1: 8, nota2: 10}
];

function calcularMedia(aluno){
    return (aluno.nota1 + aluno.nota2)/2;
}

alunos.forEach(aluno =>{
    console.log(`A média de ${aluno.nome} é ${calcularMedia(aluno)}`);
});

const aprovados = alunos.filter(aluno => calcularMedia(aluno) >= 7);

const nomeAprovados = aprovados.map(aluno => aluno.nome);
console.log("Alunos aprovados: ",nomeAprovados.join(", "));
