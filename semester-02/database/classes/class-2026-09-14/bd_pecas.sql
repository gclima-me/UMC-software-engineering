-- Database
DROP DATABASE IF EXISTS vendas;

CREATE DATABASE vendas
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE vendas;

-- Table
CREATE TABLE vendedor (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(150) NOT NULL,
    comissao_pct DECIMAL(5,2) NOT NULL DEFAULT 0.00,
    PRIMARY KEY (id),
    CONSTRAINT ck_vendedor_comissao_pct CHECK (comissao_pct BETWEEN 0 AND 100)
) ENGINE=InnoDB;

CREATE TABLE armazem (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    endereco VARCHAR(150) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE cliente (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    vendedor_id INT UNSIGNED NOT NULL,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(150) NOT NULL,
    faturamento_acumulado DECIMAL(12,2) NOT NULL DEFAULT 0.00,
    limite_credito DECIMAL(12,2) NOT NULL DEFAULT 0.00,
    PRIMARY KEY (id),
    CONSTRAINT fk_cliente_vendedor 
        FOREIGN KEY (vendedor_id)
        REFERENCES vendedor (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT ck_cliente_limite CHECK (limite_credito >= 0),
    CONSTRAINT ck_cliente_faturamento CHECK (faturamento_acumulado >= 0)
) ENGINE=InnoDB;

CREATE TABLE peca (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    armazem_id INT UNSIGNED NOT NULL,
    descricao VARCHAR(120) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    qtd_estoque INT UNSIGNED NOT NULL DEFAULT 0,
    PRIMARY KEY (id),
    CONSTRAINT fk_peca_armazem 
        FOREIGN KEY (armazem_id)
        REFERENCES armazem (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT ck_peca_preco CHECK (preco >= 0),
    CONSTRAINT ck_peca_estoque CHECK (qtd_estoque >= 0)
) ENGINE=InnoDB;

CREATE TABLE pedido (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    cliente_id INT UNSIGNED NOT NULL,
    data_pedido DATE NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_pedido_cliente 
        FOREIGN KEY (cliente_id)
        REFERENCES cliente (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE item_pedido (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    pedido_id INT UNSIGNED NOT NULL,
    peca_id INT UNSIGNED NOT NULL,
    quantidade INT UNSIGNED NOT NULL,
    preco_cotado DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT uq_item_pedido_pedido_id_peca_id UNIQUE (pedido_id, peca_id),
    CONSTRAINT fk_item_pedido_pedido 
        FOREIGN KEY (pedido_id)
        REFERENCES pedido (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_item_pedido_peca 
        FOREIGN KEY (peca_id)
        REFERENCES peca (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT ck_item_pedido_quantidade CHECK (quantidade > 0)
) ENGINE=InnoDB;