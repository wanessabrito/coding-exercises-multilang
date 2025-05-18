package uninter;

public abstract class Moeda {
	protected double valor;

	public Moeda(){}
	
	public Moeda(double valor) {
		super();
		this.valor = valor;
	}
	
	// Método abstrato que deverá ser implementado nas subclasses (Real, Dolar, Euro)
	public abstract String info();
	
	public abstract double converter();

	public double getValor(){
		return valor;
	}

	// Setter para o valor, com verificação se o valor é negativo
	public void setValor(double valor) throws Exception{
		if(valor < 0){
			throw new Exception("Valor não pode ser negativo");
		}
		this.valor = valor;
	}
}
