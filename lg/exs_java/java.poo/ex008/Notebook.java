package empresa;

public class Notebook  extends Computador{
	
	int polegadasTela;
	
	public Notebook(int gbMemoria, int processadores, int polegadasTela) {
		super(gbMemoria, processadores);
		this.polegadasTela = polegadasTela;	
	}

	@Override
	double calcularValor() {
		double total = (250 * gbMemoria) + (500 * processadores) + (100 * polegadasTela);
		return total;
	}

}
