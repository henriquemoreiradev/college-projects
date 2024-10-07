import java.util.Scanner;

public class Teste {
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Digite o seu nome: ");
		String nome = scanner.next();
		System.out.println("O nome lido foi " + nome);
		
		System.out.println();
		System.out.print("Digite a sua idade: ");
		int minhaIdade = scanner.nextInt();
		System.out.println("A idade lida foi " + minhaIdade);
		
		scanner.close();
	}
}

