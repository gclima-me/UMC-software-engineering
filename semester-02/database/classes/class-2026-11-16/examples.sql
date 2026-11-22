-- esse arquivo não tem nenhuma conexão com schema.sql, servindo apenas para o entendimento da estrutura de uma trigger.

-- trigger
DELIMITER //

CREATE TRIGGER tg_nome_trigger
AFTER INSERT ON tabela_alvo
FOR EACH ROW
BEGIN
	-- intruções aqui
END //

CREATE TRIGGER tg_baixar_estoque_pedido
AFTER INSERT ON pedido
FOR EACH ROW
BEGIN
	UPDATE produto
    SET estoque_qtd = estoque_qtd - NEW.quantidade
    WHERE produto_id = NEW.produto_id
END //

CREATE TRIGGER tg_validar_estoque_antes_venda
BEFORE INSERT ON pedido
FOR EACH ROW
BEGIN
	DECLARE v_estoque INT;
    SELECT estoque_qtd INTO v_estoque
    FROM produtos
    WHERE produto_id = NEW.produto_id;
END //

DELIMITER ;

SHOW CREATE TRIGGER tg_baixar_estoque_pedido;