USE view_db;

DROP PROCEDURE IF EXISTS sp_registrar_venda;
DROP PROCEDURE IF EXISTS sp_finalizar_pedido;

DELIMITER //

-- Exercício 3: Processamento Seguro de Vendas

-- Realizar uma venda requer atualizar o estoque e registrar o item.
CREATE PROCEDURE sp_registrar_venda (
    IN p_pedido_id INT UNSIGNED,
    IN p_produto_id INT UNSIGNED,
    IN p_quantidade INT UNSIGNED
)
BEGIN
    DECLARE v_estoque_atual INT UNSIGNED;
    DECLARE v_preco_atual DECIMAL(10, 2);

    -- Verifica o estoque e preço atual do produto
    SELECT 
        estoque, 
        preco 
    INTO 
        v_estoque_atual, 
        v_preco_atual
    FROM produto
    WHERE id = p_produto_id;

    -- Validação: Retorna erro se o estoque for insuficiente.
    IF v_estoque_atual < p_quantidade THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Estoque insuficiente para realizar a venda.';
    END IF;

    -- Registra o item do pedido com o preço atual.
    INSERT INTO item_pedido
        (id_pedido, id_produto, quantidade, preco_unitario)
    VALUES
        (p_pedido_id, p_produto_id, p_quantidade, v_preco_atual);

    -- Atualiza o estoque do produto.
    UPDATE produto
    SET estoque = estoque - p_quantidade
    WHERE id = p_produto_id;

END//

-- Exercício 4: Atualização em Lote de Status

-- A equipe de logística precisa de um comando rápido para fechar pedidos pendentes.
CREATE PROCEDURE sp_finalizar_pedido (
    IN p_pedido_id INT UNSIGNED
)
BEGIN
    DECLARE v_status_atual VARCHAR(20);

    -- Verifica o status atual do pedido.
    SELECT 
        status_pedido 
    INTO 
        v_status_atual
    FROM pedido
    WHERE id = p_pedido_id;

    -- Validação: Impede a alteração se o pedido estiver cancelado.
    IF v_status_atual = 'Cancelado' THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Operação negada: O pedido já está cancelado.';
    END IF;

    -- Atualiza o status para Concluido.
    UPDATE pedido
    SET status_pedido = 'Concluido'
    WHERE id = p_pedido_id;

END//

DELIMITER ;