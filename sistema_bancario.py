pagina_inicial = (f"""------------------------------
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
------------------------------""")
deposito = 0
saque = 0
saldo = 0
limite = 500
numero_saque = 0
numero_deposito = 0
LIMITE_SAQUE = 3
extrato = ""

while True:
    print(pagina_inicial)
    menu = str(input("Digite a opção desejada: "))

    if menu == "1": #---------------DEPÓSITO--------------------
        deposito = float(input("Valor do depósito: "))
        confirmacao = str(input(f"Confirma o valor de {deposito:.2f} R$ para depositar em sua conta? S ou N: "))
        if confirmacao == "s" or "n":
            if deposito > 0:
                if confirmacao == "s":
                    saldo += deposito
                    numero_deposito += 1
                    extrato += f"Depósito: R$ {deposito:.2f}\n"
                    print("Dinheiro depositado")
                elif confirmacao == "n":
                    print("Dinheiro não depositado - Operação cancelada")
            else:
                print("Depósito inválido")
        else:
            print("Opção inválida, por favor selecione novamente a opção desejada")        

    elif menu == "2": #---------------SAQUE--------------------
        saque = float(input("Valor do saque: "))
        confirmacao = str(input(f"Confirma o valor de R$ {saque:.2f} para sacar em sua conta? S ou N: "))
        if confirmacao == ("s" or "n") and (saque > 0):
            if (limite != 0 and saque < 500) and (LIMITE_SAQUE != 0 ):
                if saldo > saque:
                    if confirmacao == "s":
                        saldo -= saque
                        limite -= saque
                        numero_saque += 1
                        LIMITE_SAQUE -= 1
                        extrato += f"Saque: R$ {saque:.2f}\n"
                        print("Dinheiro sacado")
                        print(f"Seu limite de saque diário é de: R$ {limite} e {LIMITE_SAQUE} saques.")
                    elif confirmacao == "n":
                        print("Dinheiro não sacado - Operação cancelada")
                else:
                    print("Saldo insuficiente!")
            else:
                print(f"Limite de saque diário excedido! - limite de saque é de: R$ {limite} e/ou {LIMITE_SAQUE} saques.")
        else:    
            print("Opção inválida, por favor selecione novamente a opção desejada")
        
    elif menu == "3": #---------------EXTRATO--------------------
        print(f"""\n############# EXTRATO BANCÁRIO #############
              
-Seu dinheiro total é de {saldo:.2f} reais na conta.

-Você Realizou {numero_deposito} depósitos nesse período.
-Você Realizou {numero_saque} saques nesse período\n""")
        
        print("-Não foram realizadas movimentações." if not extrato else extrato)

        print("############################################")

    elif menu == "0": #---------------SAIR--------------------
        print("Muito obrigado pela preferência! Volte sempre.")
        break

    else:
        print("Opção inválida, por favor selecione novamente a opção desejada")