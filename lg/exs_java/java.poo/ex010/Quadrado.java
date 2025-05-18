package empresa;

public class Quadrado implements Imprimivel {
	int tamanhoLado;

	public Quadrado(int tamanhoLado) {
		super();
		this.tamanhoLado = tamanhoLado;
	}

	@Override
	public void imprimir() {
		System.out.println("Quadrado");
		System.out.println("Tamando de lados: " + tamanhoLado);
	}

}
