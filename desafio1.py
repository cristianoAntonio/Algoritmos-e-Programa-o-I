#DESAFIO 1

# dias = int(input("Informe o numero de dias: "))
# producao_por_dia = 1 + 3 + 2.5
# producao_total = int(dias * producao_por_dia)
# print("Em {} dias foram produzidos {} postes".format(dias, producao_total))


#DESAFIO 2

# pedaco_tecido = int(input("Digite o numero de peças de tecido: "))
# numero_de_calcas = pedaco_tecido * 5
# tecido_desperdicado = pedaco_tecido * 11 * 0.15
# print("{} pedaços de tecido renderam {} calças e {} metros desperdicios".format(pedaco_tecido, numero_de_calcas, tecido_desperdicado))


#DESAFIO 3

# algodao = float(input("Algodao: "))
# quantidade_camisa = int(algodao/100)
# desperdicio = int(quantidade_camisa * 0.05)
# print("Com {} gramas de algodão são feitas {} camisetas e {} camisetas de desperdício".format(algodao, quantidade_camisa, desperdicio))

#DESAFIO 4

# base = float(input("base: "))
# aresta_direita = float(input("aresta_direita: "))
# aresta_esquerda = float(input("aresta_esquerda: "))
# perimetro = base+aresta_direita+aresta_esquerda
# print("Perimetro: {}".format(perimetro))

#DESAFIO 5

# horas_trabalhadas = float(input("horas trabahadas: "))
# valor_hora = float(input("valor da hora: "))
# salario_bruto = horas_trabalhadas*valor_hora
# inss = salario_bruto*0.08
# imposto_de_renda = salario_bruto*0.12
# salario_liquido = salario_bruto - inss - imposto_de_renda
# print("Salario bruto: {}\nSalario liquido: {}".format(salario_bruto, salario_liquido))

#DESAFIO 6

# tamanho_texto = int(input("Quantidade de caracteres: "))
# tempo_segundos = int(tamanho_texto / 10)
# print("Vai levar {} segundos para escrever seu texto".format(tempo_segundos))

#DESAFIO 7

# calorias_gastas = int(input("Digite quantas calorias vc deseja gastar: "))
# tempo_exercicio = calorias_gastas/500
# tempo_horas = int(tempo_exercicio)
# tempo_minutos = int((tempo_exercicio - tempo_horas)*60)
# print("Vc deve fazer {:0>2}:{:0<2} horas de exercicio para queimar {} calorias".format(tempo_horas, tempo_minutos, calorias_gastas))