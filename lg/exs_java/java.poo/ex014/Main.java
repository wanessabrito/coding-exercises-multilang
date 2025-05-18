package uninter;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
	//Método para ler um valor do tipo double e garantir que seja um valor positivo
	public static double lerValorMoeda(Scanner teclado){
		double valor = -1;
		boolean valorValido = false;
		
		while(!valorValido){
			
			try {
				valor = teclado.nextDouble();
				if(valor < 0){
					throw new Exception("Valor não poder ser negativo");
				}
				valorValido = true;// Se não der exceção, o valor é considerado válido
				
			} catch (InputMismatchException e) {
				System.out.println("Erro: Entrada inválida.");
				teclado.next();// Limpa o buffer do scanner
				
			} catch (Exception e) {
				System.out.println("Erro: " + e.getMessage());
			}
		}
		return valor;
	}

	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		
		Cofrinho cofre = new Cofrinho();// Instancia um novo objeto do tipo Cofrinho
		int escolha;
		
		do {
			// Menu principal de opções
			System.out.println();
			System.out.println("----~COFRINHO~----");
			System.out.println("1 - Adicionar Moeda");
			System.out.println("2 - Remover Moeda");
			System.out.println("3 - Listar Moedas");
			System.out.println("4 - Calcular total convertido para Real");
			System.out.println("0 - Encerrar");
			escolha = teclado.nextInt();
			
			switch(escolha) {
			case 1:// Adicionar moeda ao cofre
				System.out.println("----~Escolha a Moeda~----");
				System.out.println("1 - Real");
				System.out.println("2 - Dolar");
				System.out.println("3 - Euro");
				int tipoAdd = teclado.nextInt();
				
				System.out.println("Digite o valor: ");
				double valorAdd = lerValorMoeda(teclado);
				
				// Instancia a moeda correta de acordo com a escolha e adiciona ao cofre
				if(tipoAdd == 1) cofre.adicionar(new Real(valorAdd));
				else if(tipoAdd == 2) cofre.adicionar(new Dolar(valorAdd));
				else if(tipoAdd == 3) cofre.adicionar(new Euro(valorAdd));
				else System.out.println("Tipo inválido!");
				break;
				
			case 2:// Remover moeda do cofre
				System.out.println("----~Escolha a Moeda~----");
				System.out.println("1 - Real");
				System.out.println("2 - Dolar");
				System.out.println("3 - Euro");
				int tipoRem = teclado.nextInt();
				
				System.out.println("Digite o valor: ");
				double valorRem = lerValorMoeda(teclado);
				
				// Instancia a moeda correta e tenta remover do cofre
				if (tipoRem == 1) cofre.remover(new Real(valorRem));
				else if(tipoRem == 2) cofre.remover(new Dolar(valorRem));
				else if (tipoRem == 3) cofre.remover(new Euro(valorRem));
				else System.out.println("Tipo inválido");
				break;
				
			case 3:// Lista todas as moedas no cofre
				cofre.listagemMoedas();
				break;
				
			case 4:// Calcula e mostra o valor total convertido para reais
				System.out.printf("Total em reais no cofre: R$ %.2f\n", cofre.totalConvertido());
				break;
			
			case 0:// Encerra o programa
				System.out.println("Encerrando...");
				break;
				
			default:// Caso o usuário digite uma opção inválida
				System.out.println("Opção inválida!");
				
			}
		}while(escolha != 0); // Repete o menu até a opção 0 ser escolhida
			
		teclado.close();// Fecha o scanner para liberar recursos
	}

}
