package empresa;

public class Principal {

	public static void main(String[] args) {
		LivroDigital ld = new LivroDigital("Senhor dos aneis",
				new Autor("Tolkien","Britanico","tolkien.@gmail.com"),
				"Aventura",5,1000,3500);
		
		ld.info();
		
	}

}
