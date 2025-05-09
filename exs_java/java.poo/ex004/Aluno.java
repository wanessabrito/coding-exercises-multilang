package uninter;

public class Aluno {
	int matricula;
	String nome;
	String cpf;
	
	public Aluno() {}


	//construtor
	public Aluno(int matricula, String nome, String cpf) {
		this.matricula = matricula;
		this.nome = nome;
		this.cpf = cpf;
	}
	
	
	void info() {// método que executa uma ação (como mostrar dados), mas não devolve nenhum valor.
		System.out.println("Nome: " + nome);
		System.out.println("Matricula: " + matricula);
		System.out.println("CPF: " + cpf);
		System.out.println();
	}


}
