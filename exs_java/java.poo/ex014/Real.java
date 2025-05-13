package uninter;

public class Real extends Moeda {

	public Real() {
		super();
	}

	public Real(double valor) {
		super(valor);
	}
	
	@Override
	public String info(){
		return "Real - R$: " + this.valor;
	}
	
	@Override 
	public double converter(){
		return this.valor;
	}
	
}
