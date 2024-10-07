--  1.	Sistema de Gestão Universitária
--    Isabela Vitoriano foi contratada para desenvolver um sistema para gestão da Universidade ABC.

--  Schema SQL -----------------------------------------
--    Criar as seguintes tabelas para o sistema
--      • Alunos (MAT, nome, endereço, cidade)
--      • Disciplinas (COD_DISC, nome_disc, carga_hor)
--      • Professores (COD_PROF, nome, endereco, cidade)

create table Alunos (
	MAT int,
	nome varchar(100),
	endereço varchar(100),
  	cidade varchar(100),
	primary key(MAT)
);

create table Disciplinas (
	COD_DISC int,
	nome_disc varchar(100),
	carga_hor int,
	primary key(COD_DISC)
);

create table Professores (
	COD_PROF int,
	nome varchar(100),
	endereco varchar(100),
	cidade varchar(100),
	primary key(COD_PROF)
);

--  Query SQL ------------------------------------------
--      • Faça ao menos 3 inserções em cada uma das tabelas
insert into Alunos
  (MAT, nome, endereço, cidade)
values (1,"Romero Farias","Rua A", "Campina Grande");

insert into Alunos
  (MAT, nome, endereço, cidade)
values (2,"Elaine Moreira","Rua B", "João Pessoa");

insert into Alunos
  (MAT, nome, endereço, cidade)
values (3,"Daniel Abella","Rua C", "Patos");

insert into Disciplinas
  (COD_DISC, nome_disc, carga_hor)
values (4,"PYTHON",60);

insert into Disciplinas
  (COD_DISC, nome_disc, carga_hor)
values (5,"JAVA",80);

insert into Disciplinas
  (COD_DISC, nome_disc, carga_hor)
values (6,"SQL",100);

insert into Professores
  (COD_PROF, nome, endereco, cidade)
values (7,"Daniel","Rua D", "Campina Grande");

insert into Professores
  (COD_PROF, nome, endereco, cidade)
values (8,"Abella","Rua E", "João Pessoa");

insert into Professores
  (COD_PROF, nome, endereco, cidade)
values (9,"Zarac","Rua F", "Patos");

--      • Listar todos os alunos
select *
from Alunos;

--      • Listar todas as disciplinas
select *
from Disciplinas;

--      • Listar todos os professores 
select *
from Professores;

--      • Listar todos os alunos que residem em Campina Grande
select *
from Alunos
where cidade = "Campina Grande";

--      • Listar todos os alunos que possuem algum sobrenome Abella
select *
from Alunos
where nome like "%Abella";

--      • Listar os dados do aluno que possui matrícula 1
select *
from Alunos
where MAT = 1;

--      • Listar o nome do aluno que possui matrícula 1
select nome
from Alunos
where MAT = 1;

--      • Listar as disciplinas que possuem carga horária maior ou igual a 60
select *
from Disciplinas
where carga_hor >= 60;

--      • Listar as disciplinas que possuem no seu nome a palavra PYTHON
select *
from Disciplinas
where nome_disc = "PYTHON";

--      • Listar todos os professores que residem em Campina Grande
select *
from Professores
where cidade = "Campina Grande";

--      • Excluir o aluno que possui matrícula 2
Delete from Alunos
where MAT = 2;

--      • Excluir os alunos que possuem algum sobrenome Abella
Delete from Alunos
where nome like "%Abella";

--      • Alterar a carga horária das disciplinas com 60 horas para 80 horas
update Disciplinas
set carga_hor = 80
where carga_hor = 60;