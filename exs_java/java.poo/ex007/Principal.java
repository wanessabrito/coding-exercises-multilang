package empresa;

public class Principal {

	public static void main(String[] args) {
//		Avaliacao mario = new Avaliacao(7,4,10);
//		
//		//fazendo manualmente
//		Avaliacao luigi = new Avaliacao();
//		luigi.n1 = 8;
//		luigi.n2 = 9;
//		luigi.n3 = 10;
//		
//		
//		System.out.println("Média Aritmetica do Mario: " + mario.mediaArit());
//		System.out.println("Média Ponderada do Mario: " + mario.mediaPond());
//		System.out.println();
//		System.out.println("Média Aritmetica do Luigi: " + luigi.mediaArit());
//		System.out.println("Média Ponderada do Luigi: " + luigi.mediaPond());

		Aluno a1 = new Aluno("Mario", "Encanador",new Avaliacao(9,10,3));
		Aluno a2 = new Aluno("Luigi", "Encanador",new Avaliacao(3,2,10));
		
		a1.info();
		a2.info();
	}

}
