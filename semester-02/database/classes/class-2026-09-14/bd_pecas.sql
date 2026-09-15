CREATE DATABASE BD_VENDAS;
USE BD_VENDAS;

CREATE TABLE VENDEDOR (
    id_vendedor INT PRIMARY KEY AUTO_INCREMENT,
    nome_vendedor VARCHAR(100) NOT NULL,
    endereco_vendedor VARCHAR(150) NOT NULL,
    comissao DECIMAL(6,2)
);

CREATE TABLE CLIENTE (
	id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome_cliente VARCHAR(100) NOT NULL,
    endereco_cliente VARCHAR(150),
	faturamento_acumulado DECIMAL(12,2),
    limite_credito DECIMAL(12,2),
    FOREIGN KEY(fk_id_vendedor) REFERENCES VENDEDOR(id_vendedor),
);

CREATE TABLE PECA (
	id_peca INT PRIMARY KEY AUTO_INCREMENT,
    descricao_peca VARCHAR(120) NOT NULL,
    preco_peca DECIMAL(10,2) NOT NULL,
    quantidade_estoque INT NOT NULL,
    FOREIGN KEY(fk_id_armazem) REFERENCES ARMAZEM(id_armazem)
);

CREATE TABLE ARMAZEM (
	id_armazem INT PRIMARY KEY AUTO_INCREMENT,
    endereco_armazem VARCHAR(150) NOT NULL
);

CREATE TABLE PEDIDO (
	id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    data_pedido DATETIME NOT NULL,
    FOREIGN KEY(fk_id_cliente) REFERENCES CLIENTE(id_cliente),
    FOREIGN KEY(fk_id_vendedor) REFERENCES VENDEDOR(id_vendedor),
    FOREIGN KEY(fk_id_peca) REFERENCES ITEM_PEDIDO(fk_id_peca),
);

CREATE TABLE ITEM_PEDIDO (
	fk_id_peca INT PRIMARY KEY REFERENCES PECA(id_peca),
    quantidade_peca INT NOT NULL,
    preco_cotado DECIMAL(7,2)
);