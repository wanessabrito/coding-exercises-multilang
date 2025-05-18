package empresa;

public class Principal {

	public static void main(String[] args) {
	Ingresso i = new Ingresso("ComicAnime",100);
	IngressoVip iv = new IngressoVip("ComicAnime",100,50);
	
	i.info();
	System.out.println();
	iv.info();
	
	}

}
