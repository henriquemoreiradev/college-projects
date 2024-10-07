--  2.  Sistema de Gestão de RH
--    Iasmin e Maria Luiza foram contratadas para criar um sistema de gestão de RH, necessitando criar as tabelas a seguir e, posteriormente realizar as consultas listadas as seguir:

--  Schema SQL -----------------------------------------
--    Criar as seguintes tabelas para o sistema
--      • Funcionarios (Matricula, PrimeiroNome,SegundoNome, UltimoNome, CPF, RG, Endereco, CEP,Cidade, Fone, Funcao, Salario)
--      • Departamentos (Codigo, Nome, Localizacao, NomeGerente)

create table Funcionarios (
  Matricula,
  PrimeiroNome,
  SegundoNome,
  UltimoNome,
  CPF,
  RG,
  Endereco,
  CEP,
  Cidade,
  Fone,
  Funcao,
  Salario,
	primary key(Matricula)
);

create table Departamentos (
  Codigo,
  Nome,
  Localizacao,
  NomeGerente,
  primary key(Codigo)
);

--  Query SQL ------------------------------------------
--      • Listar nome e sobrenome dos funcionários ordenado por sobrenome
select PrimeiroNome, UltimoNome
from Funcionarios
order by UltimoNome;

--      • Listar todos os campos de funcionários ordenados por cidade
select *
from Funcionarios
order by Cidade;

--      • Liste os funcionários que têm salário superior a R$ 1.000,
select *
from Funcionarios
where Salario > 1000;

--      • Liste o primeiro nome dos funcionários
select PrimeiroNome
from Funcionarios;

--      • Liste o total da folha de pagamento (usando sum)
select sum(Salario) as FolhaDePagamento
from Funcionarios;

--      • Liste a quantidade de funcionários desta empresa (usando count)
select count(Matricula)
from Funcionarios