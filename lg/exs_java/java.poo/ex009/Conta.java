package empresa;

public class Conta {
	String nome;
	double saldo;
	
	public Conta(String nome, double saldo) {
		super();
		this.nome = nome;
		this.saldo = saldo;
	}
	
	public void depositar(double valor) throws Exception {
		if(valor < 0) {
			throw new Exception("Valor invalido");
		}
		saldo += valor;
	}
	
	public void sacar(double valor) throws Exception {
		
		if(valor > saldo) {
			throw new Exception("Saldo insuficiente");
		}
		if(valor < 0) {
			throw new Exception("Valor invalido");
		}
		saldo -= valor;
	}
	
	public void tranferir(double valor,Conta destino) throws Exception {
		this.sacar(valor);
		destino.depositar(valor);
		
	}
	
	public void info() {
		System.out.println("--------------");
		System.out.println("Nome: " + nome);
		System.out.println("Saldo: " + saldo);
	}
	

}
