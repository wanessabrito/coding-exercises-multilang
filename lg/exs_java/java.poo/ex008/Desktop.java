package empresa;

public class Desktop extends Computador {

	double acessorios;
	
	public Desktop(int gbMemoria, int processadores, double acessorios) {
		super(gbMemoria, processadores);
		this.acessorios = acessorios;
	}
	
	@Override
	double calcularValor() {
		double total = (200*gbMemoria) + (400*processadores) + acessorios;
		return total;
	}

}
