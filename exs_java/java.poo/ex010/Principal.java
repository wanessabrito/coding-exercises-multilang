package empresa;

public class Principal {

	public static void main(String[] args) {
		
		Funcionario f = new Funcionario("Wanessa","333-333-333-33");
		Carro c = new Carro("Honda","preto",4);
		Quadrado qd = new Quadrado(4);
		
		Imprimivel i = f;
		i.imprimir();
		
		System.out.println();
		
		i = c;
		i.imprimir();
		
		System.out.println();
		
		i = qd;
		i.imprimir();

	}

}
