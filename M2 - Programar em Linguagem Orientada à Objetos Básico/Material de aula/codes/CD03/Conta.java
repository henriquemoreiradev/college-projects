public class Conta {

	static int numeroConta;
	int numeroAgencia;
	String titular;
	double saldo;
	
	public static void main(String[] args) {
		
		Conta novaConta1 = new Conta();
		novaConta1.numeroConta = 1;
		
		Conta novaConta2 = new Conta();
		
		System.out.println(novaConta1.numeroConta);
		System.out.println(novaConta2.numeroConta);
	}
}

