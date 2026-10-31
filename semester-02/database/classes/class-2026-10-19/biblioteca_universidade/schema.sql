-- Database
DROP DATABASE IF EXISTS biblioteca_universidade;

CREATE DATABASE biblioteca_universidade
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE biblioteca_universidade;

-- Table
CREATE TABLE aluno (
    ra INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    curso VARCHAR(50) NOT NULL,
    semestre TINYINT UNSIGNED NOT NULL,
    PRIMARY KEY (ra),
    CONSTRAINT ck_aluno_semestre CHECK (semestre BETWEEN 1 AND 12)
) ENGINE=InnoDB;

CREATE TABLE biblioteca (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    campus VARCHAR(100) NOT NULL,
    endereco VARCHAR(150) NOT NULL,
    telefone VARCHAR(11) NOT NULL,
    email VARCHAR(254) NOT NULL,
    responsavel VARCHAR(100) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT uq_biblioteca_email UNIQUE (email)
) ENGINE=InnoDB;

CREATE TABLE livro (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    biblioteca_id INT UNSIGNED NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    genero VARCHAR(50),
    quantidade INT UNSIGNED NOT NULL,
    isbn VARCHAR(13) NOT NULL,
    resumo VARCHAR(150) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    pagina SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT uq_livro_biblioteca_id_isbn UNIQUE (biblioteca_id, isbn),
    CONSTRAINT fk_livro_biblioteca
        FOREIGN KEY (biblioteca_id)
        REFERENCES biblioteca (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE reserva (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    data_saida DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    prev_entrega DATE NOT NULL,
    observacao VARCHAR(100),
    aluno_ra INT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_reserva_aluno
        FOREIGN KEY (aluno_ra)
        REFERENCES aluno (ra)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE item_livro (
    livro_id INT UNSIGNED NOT NULL,
    reserva_id INT UNSIGNED NOT NULL,
    quantidade INT UNSIGNED NOT NULL,
    PRIMARY KEY (livro_id, reserva_id),
    CONSTRAINT fk_item_livro_livro
        FOREIGN KEY (livro_id)
        REFERENCES livro (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_item_livro_reserva
        FOREIGN KEY (reserva_id)
        REFERENCES reserva (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
) ENGINE=InnoDB;

-- Insert
INSERT INTO biblioteca
    (campus, endereco, telefone, email, responsavel)
VALUES
    ('UMC Leste', 'Rua tal', '11009998800', 'umc.secretaria7768@example.com', 'Antonio Carlos');