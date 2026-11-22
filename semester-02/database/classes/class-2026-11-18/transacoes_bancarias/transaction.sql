USE transacoes_bancarias;

-- transaction
-- 1. Transferência via Pix com COMMIT
START TRANSACTION;

SELECT * FROM conta_bancaria;

-- debita R$ 300,00 da conta de Ana
UPDATE conta_bancaria
SET saldo = saldo - 400.00
WHERE id = 1;

-- credita R$ 300,00 na conta de Bruno
UPDATE conta_bancaria
SET saldo = saldo + 300.00
WHERE id = 2;

COMMIT; -- efetiva permanentemente as duas operações

SELECT * FROM conta_bancaria;

-- 2. Reversão de anomalia em transação com ROLLBACK
START TRANSACTION;

-- zera a conta da Ana por engano
UPDATE conta_bancaria
SET saldo = 0.00
WHERE id = 1;

SELECT * FROM conta_bancaria;

ROLLBACK; -- cancela e restaura o estado anterior ao START

SELECT * FROM conta_bancaria;

-- 3. Retornar transação efetivada com ROLLBACK TO SAVEPOINT
START TRANSACTION;

INSERT INTO conta_bancaria
	(nome, saldo)
VALUES
	('Carla Dias', 1254.64);
    
SAVEPOINT sv_conta_criada; -- cria ponto de retorno nomeado

INSERT INTO conta_bancaria
	(nome, saldo)
VALUES
	('Cliente Teste', 9999.99);
    
SELECT * FROM conta_bancaria;
    
ROLLBACK TO SAVEPOINT sv_conta_criada; -- desfaz apenas o Cliente Teste, mantendo a Carla

COMMIT; -- encerra a transação

SELECT * FROM conta_bancaria;