public class Teste {

	public static void main(String[] args) {
		
		Carro carro1 = new Carro("Audi A3", 2019);
		Carro carro2 = new Carro("Jetta", 2023);
		
		System.out.println(carro1.quantidadeVendas);
		System.out.println(carro2.quantidadeVendas);
		System.out.println(Carro.quantidadeVendas);
		
		
		System.out.println(carro1.mostrarQuantidadeVendas());
		System.out.println(carro2.mostrarQuantidadeVendas());
		System.out.println(Carro.mostrarQuantidadeVendas());
	}
}
