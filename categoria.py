"""Uma empresa precisa que quando o usuario digitar o numero 1, o programa imprimira a palavra "Alimentos""
Se o usuario digitar o numero 2, imprimira a palavra "Bebidas" 
Se o usuario digitar o numero 3 ou 4, imprimirá a palavra "Cosmeticos"
Se o usuario digitar o numero 5 ou 6, imprimirá a palavra "Produtos de Limpeza"
Qualquer outro, o programa imprimirá "Categoria não encontrada"
"""""


categoria = int (input("Favor informe a categoria: "))
match categoria:
    case 1:
         print ("Alimentos")
    case 2:
         print ("Bebidas")
    case 3|4:
         print ("Cosmeticos")
    case 5|6:
         print (" Produtos de Limpeza")    
    case _:
        print ("Categoria invalida")      
