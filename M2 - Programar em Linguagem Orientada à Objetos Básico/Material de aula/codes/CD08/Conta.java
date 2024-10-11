public class Conta {

	public int numeroConta;
	public int numeroAgencia;
	public String titular;
	public double saldo;

	public Conta(int numeroConta, int numeroAgencia, String titular, double saldo) {
		this.numeroConta = numeroConta;
		this.numeroAgencia = numeroAgencia;
		this.titular = titular;
		this.saldo = saldo;
	}

	public Conta(int numeroConta, int numeroAgencia, String titular) {
		this.numeroConta = numeroConta;
		this.numeroAgencia = numeroAgencia;
		this.titular = titular;
	}

}
