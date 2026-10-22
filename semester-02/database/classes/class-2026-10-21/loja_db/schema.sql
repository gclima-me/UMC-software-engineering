-- =====================================
-- 1. CRIAÇÃO DO BANCO DE DADOS
-- =====================================
DROP DATABASE IF EXISTS loja_db;
CREATE DATABASE loja_db;
USE loja_db;

-- =====================================
-- 2. CRIAÇÃO DAS TABELAS
-- =====================================
-- CLIENTE
CREATE TABLE cliente (
    id INT UNSIGNED AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    PRIMARY KEY(id)
) ENGINE=InnoDB;
 
-- VENDEDOR
CREATE TABLE vendedor (
    id INT UNSIGNED AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    comissao_pct DECIMAL(5,2) NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT chk_vendedor_comissao_pct CHECK (comissao_pct BETWEEN 0 AND 100) -- Verifica se a comissão está entre 0% e 100%
) ENGINE=InnoDB;

-- PEDIDO
CREATE TABLE pedido (
    id INT UNSIGNED AUTO_INCREMENT,
    data_pedido DATE NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    id_cliente INT UNSIGNED,
    id_vendedor INT UNSIGNED,
    PRIMARY KEY(id),
    CONSTRAINT chk_pedido_valor CHECK (valor >= 0), -- Impede valores negativos
    CONSTRAINT fk_pedido_cliente FOREIGN KEY (id_cliente) REFERENCES cliente(id),
    CONSTRAINT fk_pedido_vendedor FOREIGN KEY (id_vendedor) REFERENCES vendedor(id)
) ENGINE=InnoDB;
 
-- =====================================
-- 3. INSERÇÃO DE DADOS DE TESTE
-- =====================================
-- CLIENTE
INSERT INTO cliente
    (id, nome, cidade) 
VALUES 
    (1, 'Ana Silva', 'São Paulo'),
    (2, 'Bruno Costa', 'Rio de Janeiro'),
    (3, 'Carla Dias', 'Belo Horizonte'),
    (4, 'Daniel Souza', 'Curitiba');
 
-- VENDEDOR
INSERT INTO vendedor
    (id, nome, comissao_pct) 
VALUES 
    (10, 'Marcos Lima', 5.00),
    (20, 'Fernanda Alves', 7.50),
    (30, 'Ricardo Rocha', 6.00);


-- PEDIDO
INSERT INTO pedido
    (id, data_pedido, valor, id_cliente, id_vendedor)
VALUES 
    (101, '2026-03-01', 150.00, 1, 10),     -- Ana comprou com Marcos
    (102, '2026-03-02', 300.00, 1, 20),     -- Ana comprou com Fernanda
    (103, '2026-03-03', 80.00,  2, 10),     -- Bruno comprou com Marcos
    (104, '2026-03-04', 500.00, NULL, 10),  -- Pedido sem cliente cadastrado (Anônimo)
    (105, '2026-03-05', 220.00, 3, NULL);   -- Carla comprou sem vendedor atribuído