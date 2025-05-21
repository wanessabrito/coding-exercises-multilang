const tarefas = [
    {descricao: "Lavar a louça", concluida: false},
    {descricao: "Assistir aula", concluida: true},
    {descricao: "Passar a vassoura", concluida: false}
];

function listarPendentes(){
    const pendentes = tarefas.filter(tarefa => tarefa.concluida === false);
    const descricaoPendentes = pendentes.map(tarefa => tarefa.descricao);
    console.log("Tarefas Pedentes:",descricaoPendentes.join(", "));
}

function listarConcluidas(){
    const concluidas = tarefas.filter(tarefa => tarefa.concluida === true);
    const descricaoConcluidas = concluidas.map(tarefa => tarefa.descricao);
    console.log("Tarefas Concluidas:",descricaoConcluidas.join(", "));
}

listarPendentes();
listarConcluidas();
