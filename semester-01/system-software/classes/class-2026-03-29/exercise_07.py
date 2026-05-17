# Ler quatro valores numéricos inteiros e apresentar o resultado das adições e das multiplicaçõesutilizando o mesmo raciocínio aplicado quando do uso de propriedades distributivas para amáxima combinação possível entre as quatro variáveis. Não é para calcular a propriedade distributiva,apenas para usar a sua forma de combinação. Considerando a leitura de valores para asvariáveis A, B, C e D, devem ser feitas seis adições e seis multiplicações, ou seja, deve ser combinadaa variável A com a variável B, a variável A com a variável C, a variável A com a variável D.Depois é necessário combinar a variável B com a variável C e a variável B com a variável D e,por fim, a variável C será combinada com a variável D.

# Autor: Guilherme Caetano Lima

a = int(input('-- Propriedade Distributiva de 4 Variáveis --\n\nDigite o valor de A: '))

b = int(input('Digite o valor de B: '))

c = int(input('Digite o valor de C: '))

d = int(input('Digite o valor de D: '))

print(f"""
      -- RESULTADOS DAS ADIÇÕES --
      A ({a}) + B ({b}) = {a + b}
      A ({a}) + C ({c}) = {a + c}
      A ({a}) + D ({d}) = {a + d}
      B ({b}) + C ({c}) = {b + c}
      B ({b}) + D ({d}) = {b + d}
      C ({c}) + D ({d}) = {c + d}
      
      -- RESULTADOS DAS MULTIPLICAÇÕES --
      A ({a}) * B ({b}) = {a * b}
      A ({a}) * C ({c}) = {a * c}
      A ({a}) * D ({d}) = {a * d}
      B ({b}) * C ({c}) = {b * c}
      B ({b}) * D ({d}) = {b * d}
      C ({c}) * D ({d}) = {c * d}

""")