""" Uma escola solicita um porgrama que calcule e informe a media e a situação dos alunos.
Para isso o programa devera solicitar que o ususario informe as 4 notas
Se a media for maior ou igual a 7, devera informar que o aluno esta aprovado, senão, devera pedir a nota de recuperação.
O programa fara um novo calculo entre a media de a nota de recuperação, caso, esa nova media seja inferior a 5,o programa 
informará que o aluno está reprovado, senão,aprovado.
"""""

nota1 = float (input ("Aluno, informe a sua nota "))
nota2 = float (input ("Aluno, informe a sua nota "))
nota3 = float (input ("Aluno, informe a sua nota "))
nota4 = float (input ("Aluno, informe a sua nota "))

media = (nota1 + nota2 + nota3 + nota4) /4
print (f"Sua media é: {media:.2f}")
if media >= 7:
    print ("Aprovado!!!")
else:
    notarecupera = float(input ("Aluno, informe a sua nota de recuperação " ))

    mediarecupera = (media + notarecupera) / 2
    if mediarecupera <=5:
        print ("Aluno reprovado")
    else: 
        print ("Aluno aprovado")          




