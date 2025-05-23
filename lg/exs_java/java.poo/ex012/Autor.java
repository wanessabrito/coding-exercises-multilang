package empresa;

public class Autor {
	private String nome;
	private String nacionalidade;
    private String email;
    
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getNacionalidade() {
		return nacionalidade;
	}
	public void setNacionalidade(String nacionalidade) {
		this.nacionalidade = nacionalidade;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	
	public Autor(){}
	
	public Autor(String nome, String nacionalidade, String email) {
		super();
		this.nome = nome;
		this.nacionalidade = nacionalidade;
		this.email = email;
	}
	
	void info() {
		System.out.println("Nome Autor : " + nome);
		System.out.println("Nome Nacionalidade : " + nacionalidade);
		System.out.println("Nome Email : " + email);
	}
}
