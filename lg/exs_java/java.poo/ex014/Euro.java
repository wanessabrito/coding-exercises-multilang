package uninter;

public class Euro extends Moeda {

	public Euro() {
		super();
	}

	public Euro(double valor) {
		super(valor);
	}
	
	@Override
	public String info(){
		return "Euro - €: " + this.valor;
	}
	
	@Override 
	public double converter(){
		return this.valor * 6.0;
	}

}
