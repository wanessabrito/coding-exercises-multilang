package uninter;

import java.util.ArrayList;

public class Cofrinho {
	// Lista que armazena objetos do tipo Moeda (pode ser Real, Dolar ou Euro)
	private ArrayList<Moeda> moedas = new ArrayList<>();
	
	// Adiciona uma moeda ao cofrinho
	public void adicionar(Moeda moeda) {
		moedas.add(moeda);
	}
	
	// Remove uma moeda específica do cofrinho, com base na classe (tipo) e valor
	public void remover(Moeda moeda){
		moedas.removeIf(m ->
		                m.getClass().equals(moeda.getClass()) &&  // compara se é o mesmo tipo de moeda
		                m.getValor() == moeda.getValor()  // compara se tem o mesmo valor
		                );
	}
	
	// Lista as informações de todas as moedas presentes no cofre
	public void listagemMoedas(){
		if(moedas.isEmpty()) {
			System.out.println("Cofinho vazio.");
			return;
		}
		
		for(Moeda moeda: moedas) {
			System.out.println(moeda.info());
		}	
	}
	
	// Converte todas as moedas para real e retorna o valor total acumulado
	public double totalConvertido(){
		double total = 0;
		for(Moeda moeda: moedas) {
			total += moeda.converter();
		}
		return total;
	}
	
}
