public class Teste {
	public static void main(String[] args) {

		
		Conta c1 = new Conta();
		c1.depositar(1000);
		System.out.println("Saldo atual " + c1.getSaldo());
		
		c1.sacar(300);
		System.out.println("Saldo atual " + c1.getSaldo());
	}
}

