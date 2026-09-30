-- Exercício 01:
-- (Criando banco de dados)
CREATE DATABASE loja_bd;
USE loja_bd;

CREATE TABLE cliente(
	cod_cliente int,
	nome varchar(50),
	cpf varchar(14),
	rua varchar(50),
	num varchar(5),
	bairro varchar(50), 
	cidade varchar(50),
	uf varchar(2),
	cep varchar(9),
	PRIMARY KEY (cod_cliente)
);

-- Exercício 02:
-- (Correto)
INSERT INTO cliente (cod_cliente, nome, cpf, rua, num, bairro, cidade, uf, cep)
	VALUES (1, 'GILBERTO','12345678901', 'Av. Astronautas', '1333', 'Cidade Jardim','S.J. dos Campos', 'SP','12227-220');

-- (Concertando CPF duplicado, alterando de 1 para 2)
INSERT INTO cliente (cod_cliente, nome, cpf, rua, num, bairro, cidade, uf, cep)
	VALUES (2,'EDUARDO','12345678902', 'Av.X', '1456', 'Vila', 'Rio de Janeiro', 'RJ', '35000000');

-- Exercício 03:
-- (Concertando CPF duplicado, alterando de 1 para 2)
INSERT INTO cliente
    VALUES (3, 'BRUNO','12345678902', 'Rua General', '195', 'Vila Azul', 'Ouro Preto', 'MG', '35400-000');

-- (Concertando especificação não-procedural para procedural)
INSERT INTO cliente (cod_cliente, nome, cpf, rua)
    VALUES (4, 'RICARDO','12345678903', 'Rua Esquerda');

-- (Concertando especificação não-procedural para procedural e incluindo cod_cliente, pois não é auto_increment)
INSERT INTO cliente (cod_cliente, nome, cpf)
    VALUES (5, 'ANTONIO','12345678904');

-- Exercício 04:
-- (Correto, mas não há clientes com código menor que zero)
DELETE FROM cliente WHERE cod_cliente < 0;

-- (Correto, mas o SGBD impede exclusão por segurança)
DELETE FROM cliente WHERE nome = 'bruno';

-- (Concertando falta de * e ;)
DELETE * FROM cliente;

-- Exercício 05:
-- (Correto)
UPDATE cliente SET nome = 'João' WHERE cod_cliente = 0;
-- (Correto, mas o SGBD impede exclusão por segurança)
UPDATE cliente SET nome = 'João' WHERE nome = 'Bruno'