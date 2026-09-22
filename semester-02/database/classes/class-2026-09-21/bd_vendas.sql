-- =====================================================================
-- Banco de Dados - Exercicio de Modelagem: Vendedor / Cliente / Pecas / Pedidos
-- =====================================================================

DROP DATABASE IF EXISTS bd_vendas;

CREATE DATABASE bd_vendas

  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE bd_vendas;

-- ---------------------------------------------------------------------
-- VENDEDOR
-- ---------------------------------------------------------------------
CREATE TABLE vendedor (
  codigo    INT           NOT NULL AUTO_INCREMENT,
  nome      VARCHAR(100)  NOT NULL,
  endereco  VARCHAR(150)  NOT NULL,
  comissao  DECIMAL(5,2)  NOT NULL DEFAULT 0.00,
  CONSTRAINT pk_vendedor       PRIMARY KEY (codigo),

  CONSTRAINT ck_vend_comissao  CHECK (comissao >= 0 AND comissao <= 100)
) ENGINE=InnoDB;


-- ---------------------------------------------------------------------
-- ARMAZEM
-- ---------------------------------------------------------------------
CREATE TABLE armazem (
  codigo    INT           NOT NULL AUTO_INCREMENT,
  endereco  VARCHAR(150)  NOT NULL,
  CONSTRAINT pk_armazem PRIMARY KEY (codigo)
) ENGINE=InnoDB;

-- ---------------------------------------------------------------------
-- CLIENTE
-- Um cliente é atendido por EXATAMENTE UM vendedor -> FK obrigatoria (NOT NULL)
-- ---------------------------------------------------------------------
CREATE TABLE cliente (
  codigo            INT            NOT NULL AUTO_INCREMENT,
  nome              VARCHAR(100)   NOT NULL,
  endereco          VARCHAR(150)   NOT NULL,
  faturamento_acum  DECIMAL(12,2)  NOT NULL DEFAULT 0.00,
  limite_credito    DECIMAL(12,2)  NOT NULL DEFAULT 0.00,
  cod_vendedor      INT            NOT NULL,
  CONSTRAINT pk_cliente      PRIMARY KEY (codigo),
  CONSTRAINT fk_cli_vendedor FOREIGN KEY (cod_vendedor)
    REFERENCES vendedor (codigo)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CONSTRAINT ck_cli_limite   CHECK (limite_credito >= 0),
  CONSTRAINT ck_cli_fatur    CHECK (faturamento_acum >= 0)
) ENGINE=InnoDB;

CREATE INDEX ix_cliente_vendedor ON cliente (cod_vendedor);

-- ---------------------------------------------------------------------
-- PECA
-- Uma peca esta estocada em UM UNICO armazem -> FK simples em peca
-- ---------------------------------------------------------------------
CREATE TABLE peca (
  codigo        INT            NOT NULL AUTO_INCREMENT,
  descricao     VARCHAR(120)   NOT NULL,
  preco         DECIMAL(10,2)  NOT NULL,
  qtd_estoque   INT            NOT NULL DEFAULT 0,
  cod_armazem   INT            NOT NULL,
  CONSTRAINT pk_peca        PRIMARY KEY (codigo),
  CONSTRAINT fk_peca_armaz  FOREIGN KEY (cod_armazem)
    REFERENCES armazem (codigo)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CONSTRAINT ck_peca_preco  CHECK (preco >= 0),
  CONSTRAINT ck_peca_estoq  CHECK (qtd_estoque >= 0)
) ENGINE=InnoDB;

CREATE INDEX ix_peca_armazem ON peca (cod_armazem);

-- ---------------------------------------------------------------------
-- PEDIDO
-- Ha somente UM cliente e UM vendedor por pedido.
-- Nome/endereco do cliente NAO sao copiados aqui: vem por JOIN.
-- ---------------------------------------------------------------------
CREATE TABLE pedido (
  numero        INT       NOT NULL AUTO_INCREMENT,
  data_pedido   DATE      NOT NULL,
  cod_cliente   INT       NOT NULL,
  cod_vendedor  INT       NOT NULL,
  CONSTRAINT pk_pedido       PRIMARY KEY (numero),
  CONSTRAINT fk_ped_cliente  FOREIGN KEY (cod_cliente)
    REFERENCES cliente (codigo)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CONSTRAINT fk_ped_vendedor FOREIGN KEY (cod_vendedor)
    REFERENCES vendedor (codigo)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE INDEX ix_pedido_cliente  ON pedido (cod_cliente);
CREATE INDEX ix_pedido_vendedor ON pedido (cod_vendedor);

-- ---------------------------------------------------------------------
-- ITEM_PEDIDO  (resolve o N:M entre PEDIDO e PECA)
-- preco_cotado e ARMAZENADO porque pode diferir de peca.preco (dado historico)
-- ---------------------------------------------------------------------
CREATE TABLE item_pedido (
  num_pedido    INT            NOT NULL,
  cod_peca      INT            NOT NULL,
  quantidade    INT            NOT NULL,
  preco_cotado  DECIMAL(10,2)  NOT NULL,
  CONSTRAINT pk_item_pedido   PRIMARY KEY (num_pedido, cod_peca),
  CONSTRAINT fk_item_pedido   FOREIGN KEY (num_pedido)
    REFERENCES pedido (numero)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT fk_item_peca     FOREIGN KEY (cod_peca)
    REFERENCES peca (codigo)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CONSTRAINT ck_item_qtd      CHECK (quantidade > 0),
  CONSTRAINT ck_item_preco    CHECK (preco_cotado >= 0)
) ENGINE=InnoDB;

CREATE INDEX ix_item_peca ON item_pedido (cod_peca);

-- =====================================================================
-- DADOS DE TESTE
-- =====================================================================

INSERT INTO vendedor (codigo, nome, endereco, comissao) VALUES
  (1, 'Ana Souza',      'Rua das Acacias, 120 - Mogi das Cruzes/SP', 5.00),
  (2, 'Bruno Carvalho', 'Av. Paulista, 1500 - Sao Paulo/SP',         3.50),
  (3, 'Carla Nunes',    'Rua XV de Novembro, 45 - Suzano/SP',        7.25);

INSERT INTO armazem (codigo, endereco) VALUES
  (1, 'Rod. Ayrton Senna, km 32 - Galpao A'),
  (2, 'Av. Industrial, 900 - Galpao B');

INSERT INTO cliente (codigo, nome, endereco, faturamento_acum, limite_credito, cod_vendedor) VALUES
  (1, 'Mercearia do Ze',   'Rua Sete de Setembro, 88',  1250.00,  5000.00, 1),
  (2, 'Padaria Estrela',   'Av. Brasil, 2100',          8700.50, 10000.00, 1),
  (3, 'Bar do Joao',       'Rua das Flores, 17',         430.00,  2000.00, 2),
  (4, 'Restaurante Sabor', 'Rua Marechal Deodoro, 310', 5300.00, 15000.00, 3);

INSERT INTO peca (codigo, descricao, preco, qtd_estoque, cod_armazem) VALUES
  (1, 'Parafuso sextavado 8mm', 0.75, 5000, 1),
  (2, 'Porca sextavada 8mm',    0.40, 4200, 1),
  (3, 'Arruela lisa 8mm',       0.15, 8000, 1),
  (4, 'Chave de fenda 1/4',    18.90,  120, 2),
  (5, 'Martelo unha 27mm',     42.50,   45, 2);

INSERT INTO pedido (numero, data_pedido, cod_cliente, cod_vendedor) VALUES
  (1, '2026-09-01', 1, 1),
  (2, '2026-09-03', 2, 1),
  (3, '2026-09-08', 4, 3);

-- Note o pedido 2: preco_cotado (0.70) menor que o preco corrente (0.75).
INSERT INTO item_pedido (num_pedido, cod_peca, quantidade, preco_cotado) VALUES
  (1, 1, 100,  0.75),
  (1, 2,  80,  0.40),
  (2, 1, 500,  0.70),
  (2, 4,   2, 18.90),
  (3, 5,   3, 39.90),
  (3, 3, 200,  0.15);