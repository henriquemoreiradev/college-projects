public class Carro {

	private String descricao;
	private int ano;
	public static int quantidadeVendas;

	public Carro(String descricao, int ano) {
		this.descricao = descricao;
		this.ano = ano;
	}

	public static int mostrarQuantidadeVendas() {
		return quantidadeVendas;
	}
}
