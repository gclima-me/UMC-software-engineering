-- Banco de Dados
DROP DATABASE IF EXISTS loja_db;

CREATE DATABASE loja_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE loja_db;

-- Tabelas
CREATE TABLE cliente (
    id INT UNSIGNED AUTO_INCREMENT,
    nome VARCHAR(150) NOT NULL,
    cpf CHAR(11) NOT NULL,
    email VARCHAR(100) NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT uq_cliente_cpf UNIQUE(cpf),
    CONSTRAINT uq_cliente_email UNIQUE(email)
) ENGINE=InnoDB;

CREATE TABLE pedido (
    id INT UNSIGNED AUTO_INCREMENT,
    cliente_id INT UNSIGNED NOT NULL,
    data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valor_total DECIMAL(10,2) NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_pedido_cliente
        FOREIGN KEY(cliente_id)
        REFERENCES cliente(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE produto (
    id INT UNSIGNED AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    PRIMARY KEY(id)
) ENGINE=InnoDB;

-- Views
CREATE VIEW vw_relatorio_vendas AS
SELECT
    p.id AS pedido_id,
    p.data_pedido,
    c.nome AS cliente,
    c.email AS email_cliente,
    p.valor_total
FROM pedido p
JOIN cliente c ON p.cliente_id = c.id;

-- Indexes
CREATE INDEX idx_pedidos_data ON pedido(data_pedido);