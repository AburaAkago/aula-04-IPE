from numpy import mean
import os
os.system('cls')
print("\tMédia Aritmética\n")
valor1 = int(input("Digite o primeiro valor:\n"))
valor2 = int(input("Digite o segundo valor:\n"))
valor3 = int(input("Digite o terceiro valor:\n"))
print("Os valores de entrada são: \n1º: ",valor1,"\n2º: ",valor2,"\n3º: ",valor3)
media = int(mean([valor1,valor2,valor3]))
print("O valor da média é: ",media)