# In[ ]:


#Calcular media dos 4 bimestres
bimestre1 = float(input("Nota do bimestre 1: "))
bimestre2 = float(input("Nota do bimestre 2: "))
bimestre3 = float(input("Nota do bimestre 3: "))
bimestre4 = float(input("Nota do bimestre 4: "))
media = (bimestre1 + bimestre2 + bimestre3 + bimestre4)/4
print("Sua media é: ", media)


# In[ ]:


#Transformar metros em centimetros
metros = float(input("Digite quantos metros você deseja converter em centimetros: "))
centimetros = metros*100
print("{0:.0f}m são {1:.0f}cm" .format(metros, centimetros)) #arrumar as casas decimais


# In[ ]:


#Peça o raio de um círculo, calcule e mostre sua área
import math
math.pi
raio = float(input("Digite o raio do circulo: "))
area = math.pi*raio**2
print("A area do circulo é: {0:.1f}" .format(area))


# In[ ]:


#Calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
lado = float(input("Digite quanto mede o lado do quadrado: "))
area = lado**2
print("O dobro da area do quadrado é:{0} " .format(area*2)) #arrumar casas decimais


# In[ ]:


#Quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês
salariohora = float(input("Qual o valor recebido por hora? "))
horastrabalhadas = int(input("Quantas horas trabalhadas no mês? "))
salariomes = salariohora*horastrabalhadas
print("Seu salario no mês é: {0} reais" .format(salariomes)) #arrumar casas decimais


# In[ ]:


#Peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius
grausFarenheit = int(input("Digite a temperatura Farenheit: "))
grausCelsius = (5*(grausFarenheit-32)/9)
print("A temperatura em Celsius é: ", grausCelsius)


# In[ ]:


#Peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit
grausCelsius = int(input("Digite a temperatua Celsius: "))
grausFarenheit = grausCelsius*(9/5)+32
print("A temperatura em Farenheit é: ",grausFarenheit)


# In[ ]:


#Peça 2 números inteiros e um número real. Calcule e mostre
inteiro1 = int(input("Digite o primeiro numero inteiro: "))
inteiro2 = int(input("Digite o segundo numero inteiro: "))
numReal = float(input("Digite um numero real: "))
conta1 = (inteiro1*2)*(inteiro2/2) #o produto do dobro do primeiro com metade do segundo
conta2 = (inteiro1*3)+numReal #a soma do triplo do primeiro com o terceiro
conta3 = numReal**3 #o terceiro elevado ao cubo
print("o produto do dobro do primeiro com metade do segundo é: ", conta1)
print("a soma do triplo do primeiro com o terceiro é: ", conta2)
print("o terceiro elevado ao cubo é: ", conta3)


# In[ ]:


#Entre com a altura de uma pessoa, calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input("Digite sua altura em metros: "))
pesoideal = (72.7*altura)-58
print("Seu peso ideal é: {0:.1f}" .format(pesoideal))


# In[ ]:


#Entre com a altura de uma pessoa, calcule seu peso ideal, utilizando as seguintes fórmulas: H:(72.7*h)-58 M:(62.1*h)-44.7
altura = float(input("Digite sua altura em metros: "))
s = input("Digite se você é homem ou mulher: ")
h = (72.7*altura)-58
m = (62.1*altura)-44.7
if s == "homem":
    print("Seu peso ideal é: {0:.1f}" .format(h))
else:
    print("Seu peso ideal é: {0:.1f}" .format(m))


# In[ ]:


#Entre com peso e calcule o excesso. Gravar excesso a quantidade além do limite e o valor da multa que João deverá pagar.
pesopeixe = float(input("Digite o peso do peixe: "))
excesso = pesopeixe-50
multa = excesso*4
if pesopeixe <= 50:
    print("Você não foi multado!")
else:
    print("Você excedeu em {} kg o peso permitido!" .format(excesso))
    print("Você foi multado em: {} reais" .format(multa))


# In[ ]:


#Quanto recebe por hora, horas trabalhadas no mês. Mostre o salário no mês, com descontados 11% IR, 8% INSS e 5% sindicato
salarioHora = float(input("Digite o salario recebido por hora: "))
horasMes = float(input("Digite quantas horas trabalhadas no mês: "))
salarioTotal = salarioHora*horasMes
imposRenda = salarioTotal*(11/100)
inss = salarioTotal*(8/100)
sindicato = salarioTotal*(5/100)
salarioLiq = salarioTotal-(imposRenda+inss+sindicato)
print("Salario Bruto: {} reais" .format(salarioTotal))
print("IR (11%): {} reais" .format(imposRenda))
print("INSS (8%): {} reais" .format(inss))
print("Sindicato (5%): {} reais" .format(sindicato))
print("Salário Liquido: {} reais" .format(salarioLiq))


# In[ ]:


#Pedir o tamanho em m² pintado.1L para cada 3 m².Tinta é vendida latas de 18L R$80.Quant de latas de tinta compradas e valor 
import math
areaQuad = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
litrosUsados = areaQuad/3
quantLatas = math.ceil(litrosUsados/18) #"math.ceil" é usado para arredondar um numero para cima
preço = quantLatas*80

if areaQuad <= 54:
    print("Será necessario 1 lata de tinta.")
    print("Você gastou 80 reais.")
else:
    print("Será necessario {} latas de tinta." .format(quantLatas))
    print("Você gastou {} reais." .format(preço))


# In[ ]:


import math
areaQuad = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
litrosUsados = areaQuad/6
quantLatas = math.ceil(litrosUsados/18)
quantLatas2 = math.ceil(litrosUsados/3.6)
quantLatas3 = math.ceil(litrosUsados/18)/2
quantLatas4 = math.ceil(litrosUsados/3.6)/2
preço = quantLatas*80
preço2 = quantLatas2*25
preço3 = (quantLatas3*80)+(quantLatas4*25)
if areaQuad <= 108:
    print("Você tem a opção de escolher:")
    print("1 lata de tinta de 18L no valor de 80 reais.")
    print("{0} galões de 3,6L no valor de {1} reais" .format(quantLatas2, preço2))
else:
    print("Você tem a opção de escolher:")
    print("{0} lata de tinta de 18L no valor de {1} reais." .format(quantLatas, preço))
    print("{0} galões de 3,6L no valor de {1} reais" .format(quantLatas2, preço2))
    print("{0:.0f} lata de tinta de 18L e {1:.0f} galões de 3,6L totalizando {2} reais" .format(quantLatas3, quantLatas4, preço3))


# In[ ]:


#Peça o tamanho de um arquivo para download (em MB) e a velocidade da Internet, calcule o tempo de download em minutos
arquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidade = int(input("Digite a velocidade da internet em Mbps: "))
tempo = arquivo/((velocidade)/8)
print("O tempo de download é de {:.2f} minutos" .format(tempo/60))
