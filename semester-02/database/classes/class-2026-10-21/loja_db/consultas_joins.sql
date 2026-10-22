USE loja_db;

SELECT * FROM cliente;
SELECT * FROM vendedor;
SELECT * FROM pedido;

-- =====================================
-- 1. CONSULTAS COM [INNER JOIN]
-- =====================================
-- 1.1. Escreva uma consulta que exiba o nome do cliente, a data_pedido e o valor do pedido para todas as vendas em que exista um cliente cadastrado associado.
SELECT
    c.nome AS cliente, p.data_pedido, p.valor AS valor_pedido
FROM pedido p
INNER JOIN cliente c
    ON c.id = p.id_cliente;

-- 1.2. (Com 3 Tabelas) Gere um relatório completo mostrando o id_pedido, o nome do cliente, o nome do vendedor e o valor do pedido. Exiba apenas vendas onde tanto o cliente quanto o vendedor estejam identificados.
SELECT
    p.id AS id_pedido, c.nome AS cliente, v.nome AS vendedor, p.valor AS valor_pedido
FROM pedido p
INNER JOIN cliente c
    ON c.id = p.id_cliente
INNER JOIN vendedor v
    ON v.id = p.id_vendedor;

-- =====================================
-- 2. CONSULTAS COM [LEFT JOIN]
-- =====================================
-- 2.1. Listar todos os clientes cadastrados e os valores de seus respectivos pedidos (se houver).
SELECT
    c.id AS id_cliente, c.nome AS cliente, p.valor AS valor_pedido
FROM cliente c
LEFT JOIN pedido p
    ON p.id_cliente = c.id;

-- 2.2. A equipe de marketing quer identificar clientes inativos. Escreva uma consulta para listar o nome de todos os clientes que nunca realizaram nenhum pedido.
SELECT
    c.id AS id_cliente, c.nome AS cliente
FROM cliente c
LEFT JOIN pedido p
    ON p.id_cliente = c.id
WHERE
    p.id IS NULL; 

-- 2.3. Exiba o nome de cada cliente e o valor total investido em compras por ele. Clientes sem pedidos devem exibir valor zerado (0.00 ou NULL).
SELECT
    c.id AS id_cliente, c.nome AS cliente,
    COALESCE(SUM(p.valor), 0.00) AS total_gasto
FROM cliente c
LEFT JOIN pedido p
    ON p.id_cliente = c.id
GROUP BY
    c.id,
    c.nome;

-- =====================================
-- 3. CONSULTAS COM [RIGHT JOIN]
-- =====================================
-- 3.1. Escreva uma consulta utilizando RIGHT JOIN que liste o id_pedido, o valor e o nome do cliente, garantindo que todos os pedidos apareçam no resultado, mesmo os pedidos que não possuem cliente associado.
SELECT
    p.id AS id_pedido, p.valor AS valor_pedido, c.nome AS cliente
FROM cliente c
RIGHT JOIN pedido p
    ON p.id_cliente = c.id;

-- 3.2. Encontre todos os pedidos órfãos (pedidos cujo id_cliente seja nulo ou não corresponda a nenhum cliente da base), exibindo o id_pedido e o valor.
SELECT
    p.id AS id_pedido, p.valor AS valor_pedido
FROM cliente c
RIGHT JOIN pedido p
    ON c.id = p.id_cliente
WHERE
    c.id IS NULL;

-- =====================================
-- 4. CONSULTAS COM [CROSS JOIN]
-- =====================================
-- 4.1. Suponha que a empresa queira simular a alocação de todos os vendedores para todas as cidades cadastradas na tabela de clientes. Gere o produto cartesiano combinando o nome do vendedor e a cidade.
SELECT
    v.id AS id_vendedor, v.nome AS vendedor, c.cidade
FROM vendedor v
CROSS JOIN (SELECT DISTINCT cidade FROM cliente) c;

-- =====================================
-- 5. [JOIN com Filtros de Condição]
-- =====================================
-- 5.1 Liste o nome dos vendedores e o valor total vendido por cada um deles, incluindo também os vendedores que não realizaram nenhuma venda.
SELECT
    v.nome AS vendedor,
    COALESCE(SUM(p.valor), 0.00) AS total_vendido
FROM vendedor v
LEFT JOIN pedido p
    ON p.id_vendedor = v.id
GROUP BY
    v.id,
    v.nome;