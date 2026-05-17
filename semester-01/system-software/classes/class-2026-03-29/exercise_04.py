# Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, utilizando um automóvel que faz 12 quilômetros por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto (variável TEMPO) e a velocidade média (variável VELOCIDADE) durante a viagem. Desta forma, será possível obter a distância percorrida com a fórmula DISTÂNCIA <- TEMPO * VELOCIDADE. A partir do valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem com a fórmula LITROS_USADOS <- DISTÂNCIA/ 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a  quantidade de litros utilizada na viagem.

# Autor: Guilherme Caetano Lima

tempoMin = float(input('-- Calcular quantidade de litros de combustível gastos em uma viagem --\n\nDigite a duração da viagem (minutos): '))

tempoHrs = tempoMin / 60

velocidade = float(input('Digite a velocidade média da viagem (km/h): '))

distancia = tempoHrs * velocidade

litrosUsados = distancia / 12

print(f"""
      -- Resumo da viagem --
      Velocidade Média: {velocidade} km/h.
      Tempo Gasto: {tempoHrs:.2f} horas ({tempoMin} Minutos).
      Distância Percorrida: {distancia:.2f} km.
      Litros de Combustível usados: {litrosUsados:.2f} litros.
      """)