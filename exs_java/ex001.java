package empresa;

import java.util.Scanner;

public class Principal {
	
	public static void main(String[] args) {
		
		System.out.println("Digite Peso seguido de altura: ");
		Scanner teclado = new Scanner(System.in);
		int peso = teclado.nextInt();
		double altura = teclado.nextDouble();
		
		double imc = peso/ (altura * altura);
		
		System.out.printf("IMC: %.2f", imc);
	}
}
