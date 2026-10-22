DROP DATABASE IF EXISTS aula_join;
CREATE DATABASE aula_join;
USE aula_join;

CREATE TABLE cliente (
	id INT AUTO_INCREMENT,
	nome VARCHAR (100) NOT NULL,
	PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE pedido (
	id INT AUTO_INCREMENT,
	id_cliente INT,
    data_pedido DATE NOT NULL,
    valor_total DECIMAL,
	PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE funcionario (
	id INT AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    gerente VARCHAR(100),
    PRIMARY KEY(id)
)ENGINE=InnoDB;

-- Inserindo dados nas tabelas
INSERT INTO
cliente(nome)
VALUES
('Ana Silva'), ('Bruno Costa'), ('Carla Dias'), ('Daniel Souza');

INSERT INTO
pedido(id_cliente, data_pedido, valor_total)
VALUES
(1, '2026-10-16', 150), (1, '2026-10-17', 300), (2, '2026-10-17', 80), (5, '2026-10-18', 500);

INSERT INTO
funcionario(nome, gerente)
VALUES
('Carlos - Diretor', NULL),
('Mariana - Gerente', 'Carlos'),
('João - Analista', 'Mariana');

SELECT * FROM funcionario;

-- Consultas com JOINs
SELECT c.id, c.nome, p.data_pedido, p.valor_total FROM cliente c
INNER JOIN pedido p ON p.id_cliente = c.id;

SELECT c.id, c.nome, p.data_pedido, p.valor_total FROM cliente c
LEFT JOIN pedido p ON p.id_cliente = c.id;

SELECT c.id, c.nome, p.data_pedido, p.valor_total FROM cliente c
LEFT JOIN pedido p ON p.id_cliente = c.id
WHERE p.id IS NULL; -- Usando "WHERE" para consultar apenas nulos

SELECT c.id, c.nome, p.data_pedido, p.valor_total FROM cliente c
RIGHT JOIN pedido p ON p.id_cliente = c.id;

SELECT c.id, c.nome, p.data_pedido, p.valor_total FROM cliente c
FULL OUTER JOIN pedido p ON p.id_cliente = c.id;

SELECT c.id, c.nome, p.data_pedido, p.valor_total FROM cliente c
CROSS JOIN pedido p; -- CROSS JOIN não usa cláusula "ON"

SELECT c.id AS id_cliente, c.nome AS nome_cliente, p.valor_total AS pedido FROM cliente c LEFT JOIN pedido p ON c.id = p.id_cliente; -- Alias obrigatório para diferenciar a mesma tabela