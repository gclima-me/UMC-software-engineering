-- database
DROP DATABASE IF EXISTS transacoes_bancarias;

CREATE DATABASE transacoes_bancarias
	CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
    
USE transacoes_bancarias;

-- table
CREATE TABLE conta_bancaria (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    titular VARCHAR(100) NOT NULL,
    saldo DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB;

-- insert
INSERT INTO conta_bancaria
	(titular, saldo)
VALUES
	('Ana Silva', 1329.15),
    ('Bruno Costa', 523.27),
    ('Henrique Oliveira', 857.82),
    ('Júlia Carsoso', -203.56),
    ('Carlos Silva', -433.28)