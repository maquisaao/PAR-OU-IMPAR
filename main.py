# Programa: Verificar se um número é par ou ímpar

# menu 
while True:
    print("\n=== Bem-vindo ao verificador de números ===")
    print("[1] Iniciar")
    print("[2] Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        while True:
            try:
                # receber um número do usuário
                numero = int(input("Digite um número inteiro (diferente de 0): "))

                # trava se for 0
                while numero == 0:
                    print("O número não pode ser zero. Tente novamente.")
                    numero = int(input("Digite um número inteiro: "))

                # verificar se é par ou ímpar
                if numero % 2 == 0:
                    resultado = "par"
                else:
                    resultado = "ímpar"

                # imprimir o resultado
                print(f"O número {numero} é {resultado}.")

                # perguntar se quer repetir
                repetir = input("\nDeseja verificar outro número? (s/n): ").lower()
                if repetir != "s":
                    break
                # trava se for outro valor
            except ValueError:
                print("Entrada inválida. Digite apenas números inteiros.")
    #menu sair
    elif escolha == "2":
        print("Saindo... Até logo!")
        break
    else:
        print("Opção inválida, tente novamente.")
