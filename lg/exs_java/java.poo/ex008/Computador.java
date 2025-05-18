package empresa;

public abstract class Computador {
	int gbMemoria;
	int processadores;
	
	abstract double calcularValor();

	public Computador(int gbMemoria, int processadores) {
		super();
		this.gbMemoria = gbMemoria;
		this.processadores = processadores;
	}
	
}
