-- Database
DROP DATABASE IF EXISTS loja;

CREATE DATABASE loja
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE loja;

-- Table
CREATE TABLE cliente (
    id INT UNSIGNED AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE vendedor (
    id INT UNSIGNED AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    comissao_pct DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT ck_vendedor_comissao_pct CHECK (comissao_pct BETWEEN 0 AND 100)
) ENGINE=InnoDB;

CREATE TABLE pedido (
    id INT UNSIGNED AUTO_INCREMENT,
    data_pedido DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    valor DECIMAL(10,2) UNSIGNED NOT NULL,
    cliente_id INT UNSIGNED,
    vendedor_id INT UNSIGNED,
    PRIMARY KEY (id),
    CONSTRAINT fk_pedido_cliente
        FOREIGN KEY (cliente_id)
        REFERENCES cliente (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_pedido_vendedor
        FOREIGN KEY (vendedor_id)
        REFERENCES vendedor (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
) ENGINE=InnoDB;

-- Insert
INSERT INTO cliente
    (id, nome, cidade) 
VALUES 
    (1, 'Ana Silva', 'São Paulo'),
    (2, 'Bruno Costa', 'Rio de Janeiro'),
    (3, 'Carla Dias', 'Belo Horizonte'),
    (4, 'Daniel Souza', 'Curitiba');

INSERT INTO vendedor
    (id, nome, comissao_pct) 
VALUES 
    (10, 'Marcos Lima', 5.00),
    (20, 'Fernanda Alves', 7.50),
    (30, 'Ricardo Rocha', 6.00);

INSERT INTO pedido
    (id, data_pedido, valor, cliente_id, vendedor_id)
VALUES 
    (101, '2026-03-01', 150.00, 1, 10),    -- Ana comprou com Marcos
    (102, '2026-03-02', 300.00, 1, 20),    -- Ana comprou com Fernanda
    (103, '2026-03-03', 80.00,  2, 10),    -- Bruno comprou com Marcos
    (104, '2026-03-04', 500.00, NULL, 10), -- Pedido sem cliente cadastrado (Anônimo)
    (105, '2026-03-05', 220.00, 3, NULL);  -- Carla comprou sem vendedor atribuído