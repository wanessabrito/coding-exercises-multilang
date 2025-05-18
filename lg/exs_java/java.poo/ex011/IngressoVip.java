package empresa;

public class IngressoVip extends Ingresso {
	public double adicional;

	public IngressoVip() {
		super();
	}

	public IngressoVip(String nomeEvento, double valor, double adicional) {
		super(nomeEvento, valor);
		this.adicional = adicional;
	}
	
	@Override
	public void info() {
		super.info();
		System.out.println("Valor adicional: " + adicional);
		System.out.println("Valor Total: " + (valor + adicional));
	}
	
	

}
