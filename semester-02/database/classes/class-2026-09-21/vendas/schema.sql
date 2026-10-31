-- Database
DROP DATABASE IF EXISTS vendas;

CREATE DATABASE vendas
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE vendas;

-- Table e Index
CREATE TABLE vendedor (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(150) NOT NULL,
    comissao DECIMAL(5,2) NOT NULL DEFAULT 0.00,
    PRIMARY KEY (id),
    CONSTRAINT ck_vendedor_comissao CHECK (comissao BETWEEN 0 AND 100)
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

CREATE INDEX ix_cliente_vendedor ON cliente (vendedor_id);

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

CREATE INDEX ix_peca_armazem ON peca (armazem_id);

CREATE TABLE pedido (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    cliente_id INT UNSIGNED NOT NULL,
    vendedor_id INT UNSIGNED NOT NULL,
    data_pedido DATE NOT NULL,
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
        ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE INDEX ix_pedido_cliente
  ON pedido (cliente_id);

CREATE INDEX ix_pedido_vendedor
  ON pedido (vendedor_id);

CREATE TABLE item_pedido (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    pedido_id INT UNSIGNED NOT NULL,
    peca_id INT UNSIGNED NOT NULL,
    quantidade INT UNSIGNED NOT NULL,
    preco_cotado DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id),
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
    CONSTRAINT ck_item_quantidade CHECK (quantidade > 0),
    CONSTRAINT ck_item_preco_cotado CHECK (preco_cotado >= 0)
) ENGINE=InnoDB;

CREATE INDEX ix_item_pedido_pedido
  ON item_pedido (pedido_id);

CREATE INDEX ix_item_pedido_peca
  ON item_pedido (peca_id);

-- Insert
INSERT INTO vendedor
  (id, nome, endereco, comissao)
VALUES
  (1, 'Ana Souza', 'Rua das Acacias, 120 - Mogi das Cruzes/SP', 5.00),
  (2, 'Bruno Carvalho', 'Av. Paulista, 1500 - Sao Paulo/SP', 3.50),
  (3, 'Carla Nunes', 'Rua XV de Novembro, 45 - Suzano/SP', 7.25);

INSERT INTO armazem
  (id, endereco)
VALUES
  (1, 'Rod. Ayrton Senna, km 32 - Galpao A'),
  (2, 'Av. Industrial, 900 - Galpao B');

INSERT INTO cliente
  (id, nome, endereco, faturamento_acumulado, limite_credito, vendedor_id)
VALUES
  (1, 'Mercearia do Ze', 'Rua Sete de Setembro, 88', 1250.00, 5000.00, 1),
  (2, 'Padaria Estrela', 'Av. Brasil, 2100', 8700.50, 10000.00, 1),
  (3, 'Bar do Joao', 'Rua das Flores, 17', 430.00, 2000.00, 2),
  (4, 'Restaurante Sabor', 'Rua Marechal Deodoro, 310', 5300.00, 15000.00, 3);

INSERT INTO peca
  (id, descricao, preco, qtd_estoque, armazem_id)
VALUES
  (1, 'Parafuso sextavado 8mm', 0.75, 5000, 1),
  (2, 'Porca sextavada 8mm', 0.40, 4200, 1),
  (3, 'Arruela lisa 8mm', 0.15, 8000, 1),
  (4, 'Chave de fenda 1/4', 18.90, 120, 2),
  (5, 'Martelo unha 27mm', 42.50, 45, 2);

INSERT INTO pedido
  (id, data_pedido, cliente_id, vendedor_id)
VALUES
  (1, '2026-09-01', 1, 1),
  (2, '2026-09-03', 2, 1),
  (3, '2026-09-08', 4, 3);

INSERT INTO item_pedido
  (pedido_id, peca_id, quantidade, preco_cotado)
VALUES
  (1, 1, 100, 0.75),
  (1, 2, 80, 0.40),
  (2, 1, 500, 0.70),
  (2, 4, 2, 18.90),
  (3, 5, 3, 39.90),
  (3, 3, 200, 0.15);