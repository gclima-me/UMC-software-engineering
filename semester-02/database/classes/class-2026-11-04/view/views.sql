USE view_db;

DROP VIEW IF EXISTS vw_resumo_pedido;
DROP VIEW IF EXISTS vw_produto_alerta_estoque;

-- Exercício 1: Relatório Consolidado de Pedidos

-- A equipe de atendimento precisa visualizar o resumo de todos os pedidos sem ter que escrever junções (JOIN) complexas a todo momento.
CREATE VIEW vw_resumo_pedido AS
SELECT
    p.id AS pedido_id,
    c.nome AS cliente,
    p.data_pedido,
    p.status_pedido,
    COALESCE(SUM(i.quantidade * i.preco_unitario), 0.00) AS valor_total
FROM pedido p
JOIN cliente c 
    ON p.id_cliente = c.id
LEFT JOIN item_pedido i 
    ON p.id = i.id_pedido
GROUP BY 
    p.id, 
    c.nome, 
    p.data_pedido, 
    p.status_pedido
ORDER BY 
    p.data_pedido DESC;

-- Exercício 2: Alerta de Estoque Baixo

-- O setor de compras precisa identificar rapidamente quais itens precisam de reposição urgente.
CREATE VIEW vw_produto_alerta_estoque AS
SELECT
    p.id AS produto_id,
    p.nome,
    p.estoque
FROM produto p
WHERE p.estoque <= 3;