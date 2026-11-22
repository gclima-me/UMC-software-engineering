-- database
DROP DATABASE IF EXISTS auditoria_cliente;

CREATE DATABASE auditoria_cliente
	CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
    
USE auditoria_cliente;

-- table
CREATE TABLE cliente (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    PRIMARY KEY(id)
) ENGINE=InnoDB;

CREATE TABLE log_cliente_excluido (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    data_exclusao DATETIME NOT NULL,
    PRIMARY KEY(id)
) ENGINE=InnoDB;

-- insert
INSERT INTO cliente
	(nome)
VALUES
	('Carlos'),
    ('Elisangela'),
    ('Roberto');

-- trigger
DROP TRIGGER IF EXISTS tg_auditoria_exclusao_cliente

DELIMITER //

CREATE TRIGGER tg_auditoria_exclusao_cliente
AFTER DELETE ON cliente
FOR EACH ROW
BEGIN
    INSERT INTO log_cliente_excluido
		(id, nome, data_exclusao)
    VALUES
		(OLD.id, OLD.nome, NOW());
END //

DELIMITER ;

-- delete
DELETE FROM cliente WHERE id = 1;
DELETE FROM cliente WHERE id = 2;
DELETE FROM cliente WHERE id = 3;

SHOW TRIGGERS;