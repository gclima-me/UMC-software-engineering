-- Select
SELECT 
    nome, 
    comissao
FROM vendedor;

SELECT
    cliente.nome AS cliente_nome,
    vendedor.nome AS vendedor_nome 
FROM cliente
JOIN vendedor 
    ON cliente.vendedor_id = vendedor.id
WHERE vendedor.nome = 'Ana Souza';

SELECT
    id,
    descricao,
    preco,
    qtd_estoque,
    armazem_id 
FROM peca 
WHERE qtd_estoque < 100;

SELECT
    id,
    data_pedido,
    cliente_id,
    vendedor_id 
FROM pedido 
WHERE data_pedido BETWEEN '2026-09-01' AND '2026-09-30';

-- Join
SELECT
    cliente.nome AS cliente_nome, 
    vendedor.nome AS vendedor_nome, 
    pedido.id AS pedido_id
FROM pedido 
JOIN cliente 
    ON cliente.id = pedido.cliente_id
JOIN vendedor 
    ON vendedor.id = pedido.vendedor_id;

SELECT
    pedido.id AS pedido_id, 
    pedido.data_pedido, 
    peca.descricao, 
    item_pedido.quantidade, 
    item_pedido.preco_cotado
FROM pedido
JOIN item_pedido 
    ON pedido.id = item_pedido.pedido_id
JOIN peca 
    ON item_pedido.peca_id = peca.id
WHERE pedido.id = 2;

SELECT
    pedido_id, 
    SUM(quantidade * preco_cotado) AS total
FROM item_pedido
GROUP BY pedido_id;

SELECT
    armazem.id AS cod_armazem, 
    peca.descricao AS descricao_peca
FROM item_pedido
JOIN peca 
    ON peca.id = item_pedido.peca_id
JOIN armazem 
    ON peca.armazem_id = armazem.id
WHERE item_pedido.pedido_id = 3;

-- Insert e Delete
INSERT INTO vendedor
    (nome, endereco, comissao) 
VALUES
    ('John Wick', 'Rua Nenhuma', 99.00);

DELETE FROM vendedor 
WHERE id = 1;

DELETE FROM cliente 
WHERE id = 2;

DELETE FROM pedido 
WHERE cliente_id = 2;

-- Alter e Create Table
ALTER TABLE cliente
    ADD COLUMN telefone VARCHAR(20);

CREATE TABLE transportadora (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(150) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB;

ALTER TABLE pedido
    ADD COLUMN transportadora_id INT UNSIGNED;

ALTER TABLE pedido
    ADD CONSTRAINT fk_pedido_transportadora
    FOREIGN KEY (transportadora_id)
    REFERENCES transportadora (id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT;

ALTER TABLE peca
    ADD CONSTRAINT ck_peca_preco_max CHECK (preco <= 100000.00);

INSERT INTO peca
    (id, descricao, preco, qtd_estoque, armazem_id) 
VALUES
    (6, 'Marreta', 1000000.00, 50, 2);