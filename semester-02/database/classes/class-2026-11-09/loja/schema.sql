-- database
DROP DATABASE IF EXISTS loja;

CREATE DATABASE loja
	CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
    
USE loja;

-- table
CREATE TABLE cliente (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf CHAR(11) NOT NULL,
    email VARCHAR(254) NOT NULL,
    telefone VARCHAR(11) NOT NULL,
    cep CHAR(8) NOT NULL,
    estado CHAR(2) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    rua VARCHAR(100) NOT NULL,
    numero_casa INT UNSIGNED NOT NULL,
    data_conta DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    CONSTRAINT uq_cliente_cpf UNIQUE (cpf),
    CONSTRAINT uq_cliente_email UNIQUE (email),
    CONSTRAINT uq_cliente_telefone UNIQUE (telefone)
) ENGINE=InnoDB;

CREATE TABLE produto (
	id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    nome VARCHAR(150) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    estoque INT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT ck_produto_preco CHECK (preco >= 0.00)
) ENGINE=InnoDB;

CREATE TABLE pedido (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    cliente_id INT UNSIGNED NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    data_pedido DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status_pedido CHAR(3) NOT NULL DEFAULT 'PRO', -- PRO: Processando, ENV: Enviado, CAN: Cancelado, REE: Reembolsado, ENT: Entregue, CON: Concluído.
    PRIMARY KEY (id),
    CONSTRAINT fk_pedido_cliente FOREIGN KEY (cliente_id) REFERENCES cliente(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT ck_pedido_total CHECK (total >= 0.00),
    CONSTRAINT ck_pedido_status_pedido CHECK (status_pedido IN ('PRO', 'ENV', 'CAN', 'REE', 'ENT', 'CON'))
) ENGINE=InnoDB;

CREATE TABLE item_pedido (
	id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    pedido_id INT UNSIGNED NOT NULL,
    produto_id INT UNSIGNED NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    quantidade INT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_item_pedido_pedido FOREIGN KEY (pedido_id) REFERENCES pedido(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_item_pedido_produto FOREIGN KEY (produto_id) REFERENCES produto(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT ck_item_pedido_preco_unitario CHECK (preco_unitario >= 0.00),
    CONSTRAINT ck_item_pedido_quantidade CHECK (quantidade > 0)
) ENGINE=InnoDB;