-- Database
DROP DATABASE IF EXISTS loja;

CREATE DATABASE loja
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE loja;

-- Table
CREATE TABLE cliente (
    id INT UNSIGNED NOT NULL,
    nome VARCHAR(100) NOT NULL,
    cpf CHAR(11) NOT NULL,
    rua VARCHAR(50),
    num VARCHAR(5),
    bairro VARCHAR(50), 
    cidade VARCHAR(50),
    uf CHAR(2),
    cep VARCHAR(8),
    PRIMARY KEY (id),
    CONSTRAINT uq_cliente_cpf UNIQUE (cpf)
) ENGINE=InnoDB;

-- Exercício 01:
INSERT INTO cliente 
    (id, nome, cpf, rua, num, bairro, cidade, uf, cep)
VALUES 
    (1, 'GILBERTO', '12345678901', 'Av. Astronautas', '1333', 'Cidade Jardim', 'S.J. dos Campos', 'SP', '12227-220');

INSERT INTO cliente 
    (id, nome, cpf, rua, num, bairro, cidade, uf, cep)
VALUES 
    (2, 'EDUARDO', '12345678902', 'Av. X', '1456', 'Vila', 'Rio de Janeiro', 'RJ', '35000000');

-- Exercício 02:
INSERT INTO cliente 
    (id, nome, cpf, rua, num, bairro, cidade, uf, cep)
VALUES 
    (3, 'BRUNO', '12345678903', 'Rua General', '195', 'Vila Azul', 'Ouro Preto', 'MG', '35400-000');

INSERT INTO cliente 
    (id, nome, cpf, rua)
VALUES 
    (4, 'RICARDO', '12345678904', 'Rua Esquerda');

INSERT INTO cliente 
    (id, nome, cpf)
VALUES 
    (5, 'ANTONIO', '12345678905');

-- Exercício 03:
DELETE FROM cliente 
    WHERE id < 0;

DELETE FROM cliente 
    WHERE nome = 'BRUNO';

DELETE FROM cliente;

-- Exercício 04:
UPDATE cliente 
    SET nome = 'João' 
    WHERE id = 1;

UPDATE cliente 
    SET nome = 'João' 
    WHERE nome = 'Bruno';