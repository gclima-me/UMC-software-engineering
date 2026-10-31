-- Database
DROP DATABASE IF EXISTS universidade;

CREATE DATABASE universidade
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE universidade;

-- Table
CREATE TABLE curso (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    codigo INT UNSIGNED NOT NULL,
    semestre TINYINT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT ck_curso_semestre CHECK (semestre > 0)
) ENGINE=InnoDB;

CREATE TABLE aluno (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    documento VARCHAR(20) NOT NULL,
    email VARCHAR(254) NOT NULL,
    telefone VARCHAR(11),
    data_nascimento DATE NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT uq_aluno_documento UNIQUE (documento),
    CONSTRAINT uq_aluno_email UNIQUE (email)
) ENGINE=InnoDB;

CREATE TABLE professor (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(254) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT uq_professor_email UNIQUE (email)
) ENGINE=InnoDB;

CREATE TABLE disciplina (
    id INT UNSIGNED AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    codigo SMALLINT UNSIGNED NOT NULL,
    carga_horaria SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT ck_disciplina_carga CHECK (carga_horaria > 0)
) ENGINE=InnoDB;

CREATE TABLE turma (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    id_disciplina INT UNSIGNED NOT NULL,
    id_professor INT UNSIGNED NOT NULL,
    id_curso INT UNSIGNED NOT NULL,
    periodo INT UNSIGNED NOT NULL,
    periodo_horario VARCHAR(50) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_turma_disciplina 
        FOREIGN KEY (id_disciplina)
        REFERENCES disciplina (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_turma_professor 
        FOREIGN KEY (id_professor)
        REFERENCES professor (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_turma_curso 
        FOREIGN KEY (id_curso)
        REFERENCES curso (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE matricula (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    id_aluno INT UNSIGNED NOT NULL,
    id_turma INT UNSIGNED NOT NULL,
    data_matricula DATE NOT NULL,
    nota_final DECIMAL(4,2) DEFAULT NULL,
    situacao VARCHAR(50) DEFAULT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_matricula_aluno 
        FOREIGN KEY (id_aluno)
        REFERENCES aluno (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_matricula_turma 
        FOREIGN KEY (id_turma)
        REFERENCES turma (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT uq_aluno_turma UNIQUE (id_aluno, id_turma),
    CONSTRAINT ck_matricula_nota CHECK (nota_final BETWEEN 0 AND 10 OR nota_final IS NULL)
) ENGINE=InnoDB;