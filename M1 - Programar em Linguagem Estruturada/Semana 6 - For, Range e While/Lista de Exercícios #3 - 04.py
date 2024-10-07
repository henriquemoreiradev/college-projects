#4 Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3% e que a populaçãode B seja 200.000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

populacaoPaisA = 80000
populacaoPaisB = 200000

TaxaCrescimentoPopulacaoPaisA = 1.03
TaxaCrescimentoPopulacaoPaisB = 1.015

ano = 0

while populacaoPaisA < populacaoPaisB:
  
  populacaoPaisA = populacaoPaisA*TaxaCrescimentoPopulacaoPaisA
  populacaoPaisB = populacaoPaisB*TaxaCrescimentoPopulacaoPaisB
  
  ano += 1

print(f"Sáo necessários {ano} anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento")