package uninter;

import java.util.ArrayList;

public class Principal {

	public static void main(String[] args) {
		
		Turma nova = new Turma();
		
		nova.prof = new Professor();
		nova.prof.nome = "Leornardo";
		
		nova.alunos = new ArrayList();
		nova.alunos.add(new Aluno(1004,"Wanessa","222.222.222-20"));
		
	    
	}

}
