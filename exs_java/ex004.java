package empresa;

import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		double peso = 72.5;
		int idade = 10;
		idade = idade + 2;
		String nome = "Mario";
		
		Scanner teclado = new Scanner(System.in);
		System.out.println("Digite idade, peso e nome: ");
		idade = teclado.nextInt();
		peso = teclado.nextDouble();
		nome = teclado.next();
		
		
		System.out.println("Nome: " + nome);
		System.out.printf("Idade: %d\n",idade);
		System.out.printf("Peso: %.2f",peso);
		
		if(idade < 18) {
			System.out.println("Acesso bloqueado");
		}
		else if (idade < 65) {
			System.out.println("Adulto");	
		}
		else {
			System.out.println("Adulto idoso");
		}
		
		for(int i = 0; i < 0; i++) {
			System.out.println("Valor: " + i );	
		}
		
		//array 
		//lista
		//ArrayList
		
		int megaSena[] = {11,24,31,58,65,63};
		int number[] = new int[200];
		
		number[60] = 50;
		megaSena[0] = 10;
		
	}
}
