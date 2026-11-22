USE loja;

-- function
DROP FUNCTION IF EXISTS fn_calcular_desconto_pedido;

DELIMITER //

CREATE FUNCTION fn_calcular_desconto_pedido(preco DECIMAL(10,2))
	RETURNS DECIMAL(10,2)
	DETERMINISTIC

BEGIN
	IF preco >= 3000.00 THEN
		RETURN preco * 0.85;
	ELSEIF preco >= 1000.00 THEN
		RETURN preco * 0.90;
	ELSE
		RETURN preco;
	END IF;
END //

DELIMITER ;