public class ExemploFor {
	public static void main(String[] args) {
		
		int[] numeros = {10, 20, 30, 40, 50};
		
		for (int i = 0; i < numeros.length; i++) {
			System.out.println("O elemento " + (i+1) + " da lista é " + numeros[i]);
		}
	}
}
