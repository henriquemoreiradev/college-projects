import java.util.Scanner;

public class TesteWhile {
	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		int opcao = 0;
		
		while(opcao != 3) {
			System.out.println("Opcoes");
			System.out.println("1. Opcao 1");
			System.out.println("2. Opcao 2");
			System.out.println("3. Sair");
			System.out.println("Digite a opção desejada: ");
			opcao = scanner.nextInt();
			
			System.out.println("A opção lida foi " + opcao);
		}
		
		scanner.close();
	}

}
