-- Schema SQL -----------------------------------------
create table Conta (
	numero_agencia int,
	numero_conta int,
	titular varchar(100),
	saldo float,
	primary key(numero_conta)
);

-- Query SQL ------------------------------------------
		insert into Conta
		(numero_conta, numero_agencia, titular, saldo)
		values (14,1,"Raquel Gomes", 20000);

		insert into Conta
		(numero_conta, numero_agencia, titular, saldo)
		values (15,1,"Ruth", 0);

		insert into Conta
		(numero_conta, numero_agencia, titular, saldo)
		values (16,1,"Giovana", 2000);

		insert into Conta
		(numero_conta, numero_agencia, titular, saldo)
		values (18,1,"Rafael", 101);

		insert into Conta
		(numero_conta, numero_agencia, titular, saldo)
		values (17,1,"Eduardo", 2001);

---- select from --------------------------------------
		select *
		from Conta;

---- select from where --------------------------------
		select *
		from Conta
		where saldo > 10000;

		select titular
		from Conta
		where saldo >= 1000;

---- select from where like ---------------------------
		select titular
		from Conta
		where titular like "Raquel%";

---- select from where like or ------------------------
		select titular
		from Conta
		where titular like "Daniel%" or numero_conta = 123;