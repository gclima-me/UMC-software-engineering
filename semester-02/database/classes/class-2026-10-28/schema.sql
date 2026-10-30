-- Banco de Dados
DROP DATABASE IF EXISTS loja_db;

CREATE DATABASE loja_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE loja_db;

-- Tabelas
CREATE TABLE cliente (
    id INT UNSIGNED AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT uq_cliente_email UNIQUE(email)
) ENGINE=InnoDB;

CREATE TABLE produto (
    id INT UNSIGNED AUTO_INCREMENT,
    nome_produto VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    estoque_qtd INT UNSIGNED NOT NULL,
    PRIMARY KEY(id)
) ENGINE=InnoDB;

CREATE TABLE pedido (
    id INT UNSIGNED AUTO_INCREMENT,
    cliente_id INT UNSIGNED NOT NULL,
    produto_id INT UNSIGNED NOT NULL,
    quantidade INT UNSIGNED NOT NULL,
    valor_total DECIMAL(10,2) NOT NULL,
    data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    status_pedido BOOLEAN NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_pedido_cliente
        FOREIGN KEY(cliente_id)
        REFERENCES cliente(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_pedido_produto
        FOREIGN KEY(produto_id)
        REFERENCES produto(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Procedimento
DELIMITER //

CREATE PROCEDURE sp_realizar_pedido (
    IN p_cliente_id INT UNSIGNED,
    IN p_produto_id INT UNSIGNED,
    IN p_quantidade INT UNSIGNED,
    OUT p_status BOOLEAN
)
BEGIN
    DECLARE v_estoque_atual INT UNSIGNED DEFAULT 0;
    DECLARE v_preco_unitario DECIMAL(10,2) DEFAULT 0.00;
    DECLARE v_valor_total DECIMAL(10,2) DEFAULT 0.00;
END //

DELIMITER ;