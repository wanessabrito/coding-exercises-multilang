package empresa;

public class Avaliacao {
	double n1,n2,n3;
	
	public double mediaArit() {
		
		return (n1 + n2 + n3)/3;
	}
	
	public double mediaPond() {
		return (n1*2 + n2*3 + n3*4)/9;
	}
	
	public Avaliacao() {}
	
	public Avaliacao(double n1, double n2, double n3) {
		this.n1 = n1;
		this.n2 = n2;
		this.n3 = n3;
	}

}
