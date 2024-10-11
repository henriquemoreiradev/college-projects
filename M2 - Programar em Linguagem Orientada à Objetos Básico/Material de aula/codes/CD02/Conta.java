public class Conta {

	int numeroConta;
	int numeroAgencia;
	String titular;
	double saldo;
	
	public static void main(String[] args) {
		
		Conta novaConta = new Conta();
		novaConta.numeroConta = 1;
		novaConta.titular = "Abella";
		
		System.out.println(novaConta.saldo);
		System.out.println(novaConta.titular);
		System.out.println(novaConta.numeroConta);
	}
}

