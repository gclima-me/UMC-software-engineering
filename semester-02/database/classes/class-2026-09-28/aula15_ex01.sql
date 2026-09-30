-- Criar o Banco de dados solicitado no slide 32
CREATE DATABASE Aula15_ex01;
USE Aula15_ex01;

-- Criar a tabela AlunoGrad
CREATE TABLE AlunoGrad (
    rgm_alu INT,
    nome_alu VARCHAR(50),
    endereco_alu VARCHAR(70),
    celular VARCHAR(15)
);

-- EX 01: Exibir os bancos disponíveis
SHOW DATABASES;

-- EX 02: Altere a tabela, adicionando a nova coluna dt_nascimento
ALTER TABLE Aula15_ex01.AlunoGrad
    ADD COLUMN dt_nascimento DATE;

-- EX 03: Renomeie a coluna celular para telefone_alu
ALTER TABLE Aula15_ex01.AlunoGrad
    CHANGE COLUMN celular telefone_alu VARCHAR(15);

-- EX 04: Delete a coluna dt_nascimento
ALTER TABLE Aula15_ex01.AlunoGrad
    DROP COLUMN dt_nascimento;

-- EX 05: Altere a restrição da coluna celular para que não possa ter valores nulos
ALTER TABLE Aula15_ex01.AlunoGrad
    MODIFY COLUMN telefone_alu VARCHAR(15) NOT NULL;

-- EX 06: Altere o nome da tabela para cad_alunos
ALTER TABLE Aula15_ex01.AlunoGrad
    RENAME TO cad_alunos;