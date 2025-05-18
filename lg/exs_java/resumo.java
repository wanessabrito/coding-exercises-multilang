package uninter;

import java.util.Scanner;

public class Principal {
	
	//função com retorno ==> return 
	public static float media(float a, float b,float c) {
		float result = (a + b + c)/3;
		return result;
	}
	
	//função que não retorna valor ==> void
//	public static void alo(int h) {
//		System.out.println("Fala fala galerinha");
//		if(h >= 6 && h < 12) {
//			System.out.println("Bom dia");
//		}
//		else if(h >= 12 && h <= 18) {
//			System.out.println("Boa tarde");
//		}
//		else {
//			System.out.println("Boa noite");
//		}
	public static void main(String[] args) {
		
//		System.out.println("Hello World");
//		System.out.println("Hello World");
//		
//		int idade;//4bytes
//		//inteiro => não tem parte fracionaria 
//		
//		float peso;//4bytes
//		//float => valores reais => pode representar valores com fração 
//		
//		double velocidade;//8bytes
//		char inicial = 'L';
//		
//		boolean maiorDeIdade = false;
//		
//		String nome = "Wanessa";
//		int tamanhoString = nome.length();
//		System.out.println(tamanhoString);
		
//		double resultado;
//		resultado = 4/3f; // 4/3d
//		System.out.println(resultado);
		
//		double resultado;
//		resultado = Math.pow(2,3);
//		System.out.println(resultado);

//		double resultado;
//		resultado = Math.sqrt(9);
//		System.out.println(resultado);
		
		// Pegar uma informação analogica e transformar em digital
		// Fazer a leitura da informação "input"
		// "teclado" => um objeto que foi declarado pela classe => Scanner
//		Scanner teclado = new Scanner(System.in);// entrada padrão no nosso teclado => "System.in
//		
//		int idade;
//		float altura;
//		String nome;
//		
//		System.out.println("Digite seu nome: ");
//		nome = teclado.next();
//		
//		System.out.println("Digite sua idade e altura: ");
//		idade = teclado.nextInt();
//		altura = teclado.nextFloat();
//		
//		System.out.println("Sua idade é " + idade);
//		System.out.println("Sua altura é " + altura);
		
//		Scanner teclado = new Scanner(System.in);
//		int idade;
//		
//		System.out.println("Digite sua idade: ");
//		idade = teclado.nextInt();
//		
//		if(idade < 18) {
//			System.out.println("Menor de idade");
//		}
//		else if(idade < 65) {
//			System.out.println("Adulto");
//		}
//		else {
//			System.out.println("Adulto - terceira idade");
//		}
		
//		Scanner teclado = new Scanner(System.in);
//		int idade;
//		
//		System.out.println("Digite sua idade: ");
//		idade = teclado.nextInt();
//		
//		while(idade > 0) {
//			System.out.println("Idade: " + idade );
//			idade --; // idade - idade 			
//		}
//		
//		for(int i = 0; i < 10; i ++) {
//			System.out.println("Valor: " + i);
//		}
		
		//array
//		int notas[]= {1,2,3};
//		
//		//for each 
//		for(int n : notas) {
//			System.out.println(n);
//		}
		
//		int idade = 12;
//		//and
//		if(idade > 10 && idade < 18 ) {
//			System.out.println("Estar no intervalo");
//		}
//		//or ==> pipe
//		if(idade > 10 || idade < 18) {
//			System.out.println("Estar no intervalo");
//		}
//		// not ==> !
//		
//		boolean acessoLiberado = false;
//		boolean acessoLiberado = true;
		
		//funções
		
//		alo(9);
//		alo(12);
		
		System.out.println("Media: " + media(4,5,9));
			
	}

}
