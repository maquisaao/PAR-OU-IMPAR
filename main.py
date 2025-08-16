# dizer se numero é par ou impar 

# receber um numero inteiro do usuario
numero = int(input("Digite um número inteiro: "))

# trava para caso o usuario digite 0
while numero == 0:
    print("O número não pode ser zero. Tente novamente.")
    numero = int(input("Digite um número inteiro: "))
    
# verificar se é par ou impar (divide por 2 e verifica o resto)
if numero % 2 == 0:
    resultado = "par"       
else:
    resultado = "ímpar"
# imprimir o resultado
print(f"O número {numero} é {resultado}.")

# ideias pra adicionar: looping pra seguir inserindo numeros; criar trava pra caso digite 0; criar menu para sair depois de receber o resultado



