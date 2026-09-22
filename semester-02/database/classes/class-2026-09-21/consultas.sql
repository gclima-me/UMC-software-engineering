  -- ---------------------------------------------------------------------
  -- BLOCO A - Select
  -- ---------------------------------------------------------------------
  SELECT nome, comissao FROM vendedor;
  
  SELECT * FROM cliente
  JOIN vendedor ON cliente.cod_vendedor = vendedor.codigo
  WHERE vendedor.nome = 'Ana Souza';
  
  SELECT * FROM peca WHERE qtd_estoque < 100;
  
  SELECT * FROM pedido
  WHERE data_pedido BETWEEN '1016-09-01' AND '2026-09-31'
  -- ---------------------------------------------------------------------
  -- BLOCO B - Join
  -- ---------------------------------------------------------------------
SELECT cliente.nome, vendedor.nome, pedido.numero
FROM pedido 
JOIN cliente ON cliente.codigo = pedido.cod_cliente
JOIN vendedor ON vendedor.codigo = pedido.cod_vendedor;

SELECT pedido.*, peca.descricao, item_pedido.quantidade, item_pedido.preco_cotado
FROM PEDIDO
JOIN item_pedido ON pedido.numero = item_pedido.num_pedido
JOIN peca ON item_pedido.cod_peca = peca.codigo
WHERE pedido.numero = 2;

SELECT num_pedido, SUM(quantidade * preco_cotado) AS total
FROM item_pedido
GROUP BY num_pedido;

SELECT a.codigo AS cod_armazem, p.descricao as DescricaoPeca
FROM item_pedido ip
JOIN peca p ON p.codigo = ip.cod_peca
JOIN armazem a ON p.cod_armazem = a.codigo
WHERE ip.num_pedido = 3;
  -- ---------------------------------------------------------------------
  -- BLOCO C - Regras de negócio e integridade
  -- ---------------------------------------------------------------------
  JOIN peca on item_pedido.cod_peca = peca.codigo
  WHERE pedido.numero = 2
  
  SELECT num_pedido, SUM(quantidade * preco_cotado) AS total
  FROM item_pedido
  GROUP BY num_pedido
  
  SELECT a.codigo AS cod_armazem, p.descricao AS DescricaoPeca
  FROM item_pedido ip
  JOIN peca p ON p.codigo = ip.cod_peca
  JOIN armazem a ON p.cod_armazem = a.codigo
  WHERE ip.num_pedido = 3
  
  INSERT INTO vendedor(nome, endereco, comissao)
  VALUES
  ('John Wick', 'Rua Nenhuma', 99)
  
  DELETE FROM vendedor
  WHERE codigo = 1
  
  DELETE FROM cliente
  WHERE cliente.codigo = 2
  
  DELE FROM pedido WHERE cod_cliente = 2
  -- ---------------------------------------------------------------------
  -- BLOCO D - Alterando o modelo
  -- ---------------------------------------------------------------------
  ALTER TABLE cliente
  ADD telefone VARCHAR(20)
  
  CREATE TABLE transportadora(
  codigo INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(100) NOT NULL,
  endereco VARCHAR(150) NOT NULL
  )
  
  ALTER TABLE pedido
  ADD fk_transportadora INT
  
  ALTER TABLE pedido
  ADD CONSTRAINT fk_cod_transportadora
  FOREIGN KEY (fk_transportadora)
  REFERENCES transportadora(codigo)
  
  ALTER TABLE peca
  ADD CONSTRAINT ck_peca_preco_max CHECK (preco <= 100000.00)
  
  INSERT INTO peca (codigo, descricao, preco, qtd_estoque, cod_armazem) VALUES
  (6, 'Marreta', 1000000.00,   50, 2);