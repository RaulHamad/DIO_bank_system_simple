

menu = "-----Sistema bancario-----\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\nSelecione uma opção: "
    
limite_diario_saque = 3
saldo = 0
extrato = "---Extrato bancário---\n"        
valor_max_saque_diario = 500
numero_saque = 0

while True:
   
    opcao = input(menu).lower().strip()
   

    if opcao == "d":
        try:
            deposito = float(input("Insira o valor do depósito: "))
            if deposito <= 0:
                print("Valor inválido, tente outra vez")
                print(" ")
            else:
                extrato += f'Depósito R${deposito:.2f}\n'
                saldo += deposito
        except:
            print("Valor inválido. Selecione a opção novamente")
            print(" ")
        

    elif opcao == "s":
        try:
            saque = float(input("Insira o valor do saque: "))
            
            if saque <= 0:
                print("Valor inválido, tente outra vez")
                print(" ")
            elif saque > 500 or saque > saldo:
                print("Valor acima do limite diário ou saldo disponível")
                print(" ")
            elif numero_saque > 2:
                print("Número de saque diário excedido")
                print(" ")
            else:
                extrato += f'Saque R${saque:.2f}\n'
                saldo -= saque
                numero_saque += 1
                print("Saque efetuado com sucesso!")
    
        except:
            print("Valor inválido. Selecione a opção novamente")
            print(" ")


    elif opcao == "e":
        if saldo > 0 or numero_saque > 0:
            print(extrato)
            print("---------------")
            print(f'Saldo: R${saldo:.2f}')
            print(" ")
        else:
            print("Não foram realizadas movimentações.")
            print(" ")
            
    elif opcao == 'q':
        break

    else:
        print("Opção inválida...")
