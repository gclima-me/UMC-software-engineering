-- Database
DROP DATABASE IF EXISTS aula_join;

CREATE DATABASE aula_join
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE aula_join;

-- Table
CREATE TABLE cliente (
    id INT UNSIGNED AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE pedido (
    id INT UNSIGNED AUTO_INCREMENT,
    cliente_id INT UNSIGNED,
    data_pedido DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    valor DECIMAL(10,2) UNSIGNED NOT NULL,
    PRIMARY KEY (id),
) ENGINE=InnoDB;

CREATE TABLE funcionario (
    id INT UNSIGNED AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    gerente VARCHAR(100),
    PRIMARY KEY (id)
) ENGINE=InnoDB;

-- Insert
INSERT INTO cliente
    (nome) 
VALUES 
    ('Ana Silva'), 
    ('Bruno Costa'), 
    ('Carla Dias'), 
    ('Daniel Souza');

INSERT INTO pedido
    (cliente_id, data_pedido, valor_total) 
VALUES 
    (1, '2026-10-16 00:00:00', 150.00),
    (1, '2026-10-17 00:00:00', 300.00),
    (2, '2026-10-17 00:00:00', 80.00),
    (5, '2026-10-18 00:00:00', 500.00); -- Pedido órfão (cliente 5 não existe na tabela cliente)

INSERT INTO funcionario
    (nome, gerente) 
VALUES 
    ('Carlos - Diretor', NULL),
    ('Mariana - Gerente', 'Carlos'),
    ('João - Analista', 'Mariana');

-- Inner Join
SELECT 
    c.id, 
    c.nome, 
    p.data_pedido, 
    p.valor_total 
FROM cliente c
INNER JOIN pedido p
    ON p.cliente_id = c.id;

-- Left Join
SELECT 
    c.id, 
    c.nome, 
    p.data_pedido, 
    p.valor_total 
FROM cliente c
LEFT JOIN pedido p
    ON p.cliente_id = c.id;

SELECT 
    c.id, 
    c.nome, 
    p.data_pedido, 
    p.valor_total 
FROM cliente c
LEFT JOIN pedido p
    ON p.cliente_id = c.id
    WHERE p.id IS NULL;

SELECT 
    c.id AS id_cliente, 
    c.nome AS nome_cliente, 
    p.valor_total AS pedido 
FROM cliente c 
LEFT JOIN pedido p
    ON c.id = p.cliente_id;

-- Right Join
SELECT 
    c.id, 
    c.nome, 
    p.data_pedido, 
    p.valor_total 
FROM cliente c
RIGHT JOIN pedido p
    ON p.cliente_id = c.id;

-- Full Outer Join

-- Nota: MySQL não suporta FULL OUTER JOIN nativamente. 
-- Substituído por UNION simulando a operação completa.

SELECT 
    c.id, 
    c.nome, 
    p.data_pedido, 
    p.valor_total 
FROM cliente c
LEFT JOIN pedido p
    ON p.cliente_id = c.id
UNION
SELECT 
    c.id, 
    c.nome, 
    p.data_pedido, 
    p.valor_total 
FROM cliente c
RIGHT JOIN pedido p
    ON p.cliente_id = c.id;

-- Cross Join
SELECT 
    c.id, 
    c.nome, 
    p.data_pedido, 
    p.valor_total 
FROM cliente c
CROSS JOIN pedido p;