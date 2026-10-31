-- Database
DROP DATABASE IF EXISTS aluno;

CREATE DATABASE aluno
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE aluno;

-- Table
CREATE TABLE aluno_grad (
    rgm INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(100),
    celular VARCHAR(15),
    PRIMARY KEY (rgm)
) ENGINE=InnoDB;

-- Exercício 01: Exibir os bancos disponíveis
SHOW DATABASES;

-- Exercício 02: Altere a tabela, adicionando a nova coluna data_nascimento
ALTER TABLE aluno_grad
    ADD COLUMN data_nascimento DATE;

-- Exercício 03: Renomeie a coluna celular para telefone
ALTER TABLE aluno_grad
    CHANGE COLUMN celular telefone VARCHAR(11);

-- Exercício 04: Delete a coluna data_nascimento
ALTER TABLE aluno_grad
    DROP COLUMN data_nascimento;

-- Exercício 05: Altere a restrição da coluna telefone para que não possa ter valores nulos
ALTER TABLE aluno_grad
    MODIFY COLUMN telefone VARCHAR(11) NOT NULL;

-- Exercício 06: Altere o nome da tabela para cad_aluno
ALTER TABLE aluno_grad
    RENAME TO cad_aluno;