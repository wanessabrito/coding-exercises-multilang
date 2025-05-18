package empresa;

public class Carro {
	String nome;
	String modelo;
	float velocidade;
	
	static final double PI = 3.1415;// atributo constante e que não pode ser modificado
	
	//metodo com static
	static float milhasParaMetros(float milhas) {// um comportamento que não precisa de dados de um objeto
		return milhas * 1600;
		
	}

}
