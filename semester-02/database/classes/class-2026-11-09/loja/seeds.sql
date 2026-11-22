USE loja;

-- Insert
INSERT INTO cliente 
    (nome, cpf, email, telefone, cep, estado, cidade, rua, numero_casa)
VALUES
    ('Carlos Eduardo Silva', '11111111111', 'carlos.silva@example.com', '11987654321', '00000000', 'EX', 'Cidade Fictícia Um', 'Rua de Mentira', 101),
    ('Ana Beatriz Souza', '22222222222', 'ana.souza@example.com', '11976543210', '00000000', 'EX', 'Cidade Fictícia Dois', 'Avenida Imaginária', 202),
    ('Lucas Gabriel Santos', '33333333333', 'lucas.santos@example.com', '11998765432', '11111111', 'EX', 'Cidade Fictícia Três', 'Travessa Falsa', 303);

INSERT INTO produto
    (nome, preco, categoria, estoque)
VALUES
    ('Teclado Mecânico RGB Redragon', 150.00, 'Periféricos', 50),
    ('Mouse Gamer Logitech G203', 350.50, 'Periféricos', 30),
    ('Monitor 24 Polegadas IPS Full HD', 1200.00, 'Monitores', 15);

INSERT INTO pedido
    (cliente_id, total, status_pedido)
VALUES
    (1, 505.50, 'PRO'),
    (2, 1200.00, 'CON');

INSERT INTO item_pedido
    (pedido_id, produto_id, preco_unitario, quantidade)
VALUES
    (1, 1, 150.00, 1),
    (1, 2, 350.50, 1),
    (2, 3, 1200.00, 1);