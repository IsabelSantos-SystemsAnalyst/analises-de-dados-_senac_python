## Elabore um programa que dada a idade de um nadador classifica o em uma das seguintes categorias
## Infantil A = 5 - 7 anos
## Infantil B = 8 - 10 anos
## Juvenil A  = 11 - 13 anos
## Juvenil B = 14 - 17 anos
## Adulto  =  maiores de 18 anos 

try:
idade = int (input("Ola, informe a sua idade: "))
if idade >= 5 and idade <=7:
    print("Infantil A")
elif 8<= idade <=10:
    print ("Infantil B")
elif 11<= idade <= 13:
    print ("Juvenil A")
elif 14<= idade <= 17:
    print ("Juvenil B")
elif >= 18 idade:
    print ("Adulto")
else:        
print ("SEm classificação")

print (idade)
except:
    print ("Informação invalida")



