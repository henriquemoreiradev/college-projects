public class Conta {

	public int numeroConta;
	public int numeroAgencia;
	public String titular;
	public double saldo;

	public void depositar(double montante) {

		if (montante > 0) {
			saldo += montante;
		}
	}

	public void sacar(double montante) {

		if (montante > 0) {
			saldo -= montante;
		}
	}

	public double getSaldo() {
		return saldo;
	}

	public int getNumeroConta() {
		return numeroConta;
	}

	public void setNumeroConta(int numeroConta) {
		this.numeroConta = numeroConta;
	}

	public int getNumeroAgencia() {
		return numeroAgencia;
	}

	public void setNumeroAgencia(int numeroAgencia) {
		this.numeroAgencia = numeroAgencia;
	}

	public String getTitular() {
		return titular;
	}

	public void setTitular(String titular) {
		this.titular = titular;
	}

}
