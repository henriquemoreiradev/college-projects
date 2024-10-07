#5 Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação

populacaoPaisA = int(input("Informe a população do primeiro país: "))
TaxaCrescimentoPopulacaoPaisA = float(input("Informe a taxas de crescimentodo do primeiro país em %: "))
TaxaCrescimentoPopulacaoPaisA = 1+(TaxaCrescimentoPopulacaoPaisA/100)

populacaoPaisB = int(input("Informe a população do segundo país: "))
TaxaCrescimentoPopulacaoPaisB = float(input("Informe a taxas de crescimentodo do segundo país em %: "))
TaxaCrescimentoPopulacaoPaisB = 1+(TaxaCrescimentoPopulacaoPaisB/100)

ano = 0

while populacaoPaisA < populacaoPaisB:
  
  populacaoPaisA = populacaoPaisA*TaxaCrescimentoPopulacaoPaisA
  populacaoPaisB = populacaoPaisB*TaxaCrescimentoPopulacaoPaisB
  
  ano += 1

print(f"Sáo necessários {ano} anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento")