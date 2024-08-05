#faça um programa que pergunte a hora ao usuário e, baseando se no horário descrito pelo usuário,
#exiba a saudação apropriada. Por exemplo, bom dia, se o usuário digitar a hora entre 0 e 11. 
#Boa tarde, Se o usuário digitar a hora entre 12 e 17 Boa noite. Se o usuário digitar a hora entre 18 e 23

try:

 digite_hora = float(input('Informe o horário: '))

 if 0 <= digite_hora < 12: #condições para bom dia
     print('Bom dia!')

 elif 12 <= digite_hora <= 18: #condições para boa tarde
     print('Boa tarde!')

 elif 18 < digite_hora <= 23: #condições para boa noite
     print('Boa noite!')

except:
   print('Informe um número válido! ')