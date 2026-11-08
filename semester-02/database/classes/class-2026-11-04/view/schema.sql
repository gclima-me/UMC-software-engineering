-- Database
DROP DATABASE IF EXISTS view_db;

CREATE DATABASE view_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE view_db;

-- Table
CREATE TABLE cliente (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    status_cliente VARCHAR(20) DEFAULT 'Ativo', -- 'Ativo', 'Inativo'
    PRIMARY KEY (id),
    CONSTRAINT uq_cliente_email UNIQUE (email)
) ENGINE=InnoDB;

CREATE TABLE produto (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    estoque INT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT ck_produto_preco CHECK (preco >= 0),
    CONSTRAINT ck_produto_estoque CHECK (estoque >= 0)
) ENGINE=InnoDB;

CREATE TABLE pedido (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    id_cliente INT UNSIGNED,
    data_pedido DATETIME DEFAULT CURRENT_TIMESTAMP,
    status_pedido VARCHAR(20) DEFAULT 'Pendente', -- 'Pendente', 'Concluido', 'Cancelado'
    PRIMARY KEY (id),
    CONSTRAINT fk_pedido_cliente 
        FOREIGN KEY (id_cliente) 
        REFERENCES cliente (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE item_pedido (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    id_pedido INT UNSIGNED,
    id_produto INT UNSIGNED,
    quantidade INT UNSIGNED NOT NULL,
    preco_unitario DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_item_pedido_pedido 
        FOREIGN KEY (id_pedido) 
        REFERENCES pedido (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_item_pedido_produto 
        FOREIGN KEY (id_produto) 
        REFERENCES produto (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT ck_item_pedido_quantidade CHECK (quantidade > 0),
    CONSTRAINT ck_item_pedido_preco CHECK (preco_unitario >= 0)
) ENGINE=InnoDB;

-- Insert
INSERT INTO cliente
    (nome, email, status_cliente)
VALUES
    ('Ana Silva', 'ana@email.com', 'Ativo'),
    ('Carlos Souza', 'carlos@email.com', 'Ativo'),
    ('Beatriz Lima', 'beatriz@email.com', 'Inativo');

INSERT INTO produto
    (nome, preco, estoque)
VALUES
    ('Notebook Pro', 4500.00, 10),
    ('Mouse Sem Fio', 120.00, 50),
    ('Teclado Mecânico', 350.00, 2),
    ('Monitor 27"', 1400.00, 0);

INSERT INTO pedido
    (id_cliente, data_pedido, status_pedido)
VALUES
    (1, '2026-11-04 19:32:49', 'Concluido'),
    (2, '2026-11-02 19:32:49', 'Pendente');

INSERT INTO item_pedido
    (id_pedido, id_produto, quantidade, preco_unitario)
VALUES
    (1, 1, 1, 4500.00),
    (1, 2, 2, 120.00),
    (2, 3, 1, 350.00);