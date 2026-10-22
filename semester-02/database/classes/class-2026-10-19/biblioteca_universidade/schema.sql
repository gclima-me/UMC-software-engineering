CREATE DATABASE IF NOT EXISTS biblioteca_universidade;
USE biblioteca_universidade;

CREATE TABLE IF NOT EXISTS aluno (
	ra INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome_completo VARCHAR(100),
    curso VARCHAR(50),
    semestre CHAR(2)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS biblioteca (
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    campus VARCHAR(50) NOT NULL,
    endereco VARCHAR(150) NOT NULL,
    telefone VARCHAR(11) NOT NULL,
    email VARCHAR(100) NOT NULL,
    responsavel VARCHAR(100) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS livro (
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    genero VARCHAR(50),
    quantidade INT UNSIGNED NOT NULL,
    isbn VARCHAR(13) NOT NULL,
    resumo VARCHAR(150) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    pagina INT UNSIGNED NOT NULL,
    biblioteca_id INT UNSIGNED NOT NULL,
    CONSTRAINT fk_biblioteca_id FOREIGN KEY (biblioteca_id) REFERENCES biblioteca(id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS reserva (
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	data_saida DATETIME,
    observacao VARCHAR(100),
    prev_entrega VARCHAR(8),
	aluno_ra INT UNSIGNED NOT NULL,
    CONSTRAINT fk_aluno_ra FOREIGN KEY (aluno_ra) REFERENCES aluno(ra)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS item_livro (
	quantidade INT UNSIGNED NOT NULL,
	livro_id INT UNSIGNED NOT NULL,
    reserva_id INT UNSIGNED NOT NULL,
    CONSTRAINT fk_livro_id FOREIGN KEY (livro_id) REFERENCES livro(id),
    CONSTRAINT fk_reserva_id FOREIGN KEY (reserva_id) REFERENCES reserva(id)
) ENGINE=InnoDB;