nome = input("Digite o nome do cliente: ")

print(f'''
#########################################################################
#    Bem vindo ao banco Esquina Sr(a) {nome}, escolha e digite a opção: #
#        d=Depósito                                                     #
#        s=Saque                                                        #
#        e=Extrato                                                      #
#        q=Encerrar                                                     #
#########################################################################
      ''')

saldo = 0
qtd_saque = 0
valor_max_saque = 500
qtd_max_saque = 3
extrato = ""

while True:
    opção = input("Escolha uma das opções: ")
    if opção == "d":
        depósito = float(input("Digite o valor a ser depositado: "))
        if depósito > 0:
            saldo += depósito
            print(f"Saldo em banco: R$ {saldo:7.2f}")
            extrato += f" Depósito de R$ {depósito:7.2f}\n"
        else:
            print("Valor não permitido. Refaça a operação")

    elif opção == "s":
        if qtd_saque >= qtd_max_saque:
            print(" Limite de saques permitidos extrapolados. Realize novo saque amanhã")
        else:
            sacado = float(input(" Digite o valor a ser sacado: "))
            if saldo-sacado < 0:
                print("Não há saldo suficiente para retirada")
            elif sacado > valor_max_saque:
                print(" Valor de saque maior que o permitido")
            elif sacado < 0:
                print(" Valor não permitido ou incorreto")
            else:
                saldo -= sacado
                qtd_saque += 1
                print(f"Saque de R$ {
                      sacado:7.2f} realizado. Saldo atual de:R$ {saldo:7.2f} ")
                extrato += f" Saque de R$ {sacado:7.2f}\n"

    elif opção == "e":
        print(extrato)
        print(f" O saldo atual é de R$: {saldo}")

    elif opção == "q":
        break

    else:
        print("Opção inválida. Tente novamente com as opções da tela")

print(f"Obrigado Sr(a) {nome}, por utilizar nosso banco")
