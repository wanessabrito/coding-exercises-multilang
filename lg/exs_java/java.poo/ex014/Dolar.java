package uninter;

public class Dolar extends Moeda {

	public Dolar() {
		super();
	}

	public Dolar(double valor) {
		super(valor);
	}
	
	@Override
	public String info(){
		return "Dólar - US$: " + this.valor;
	}
	
	@Override 
	public double converter(){
		return this.valor * 5.0;
	}

}
