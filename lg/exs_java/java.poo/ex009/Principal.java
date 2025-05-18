package empresa;

import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		Conta c1 = new Conta("Wanessa",5000);
		Conta c2 = new Conta("Pedro",5000);
		
		System.out.println("Digite o valor de transferência: ");
		double valorTransferir = teclado.nextDouble();
		
		boolean sucessoLeitura = false;
		while(!sucessoLeitura){
		     try {
		         c1.tranferir(valorTransferir, c2);
		         c1.info();
		         c2.info();
		         sucessoLeitura = true;
		         
		         }catch(Exception e) {
			     System.out.println("Ocorreu um problema, digite outro valor");
			     System.out.println(e.getMessage());
			     System.out.println("Digite outro valor para transferir: ");
			     valorTransferir = teclado.nextDouble();
		}
		}
	}

}
