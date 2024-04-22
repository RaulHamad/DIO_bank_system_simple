def menu():

    menu = "=====Sistema bancário=====\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\nSelecione uma opção: "
    return menu


def depositar(saldo,valor,extrato):

    try:
        
        if valor <= 0:
            print("Valor inválido, tente outra vez")
            print(" ")
        else:
            extrato += f'Depósito R${valor:.2f}\n'
            saldo += valor
            print(f'Valor depositado com sucesso.')
            print(f'Seu saldo atual é: R${saldo:.2f}')
           
    except:
        print("Valor inválido. Selecione a opção novamente")
        print(" ")
     
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    
                
    if valor <= 0:
        print("Valor inválido, tente outra vez")
        print(" ")
    elif valor > limite:
        print("Valor acima do limite diário")
        print(" ")
    elif valor > saldo:
        print("Valor acima do saldo disponível")
        print(" ")
    elif numero_saques > limite_saques:
        print("Número de saque diário excedido")
        print(" ")
    else:
        print(numero_saques,limite_saques)
        extrato += f'Saque R${valor:.2f}\n'
        saldo -= valor
        numero_saques += 1
        print("Saque efetuado com sucesso!")
        
    return saldo, extrato ,numero_saques

    


def consultar_extrato(saldo,/,*,numero_saques,extrato):

    if saldo > 0 or numero_saques > 0:
        print(extrato)
        print("===================")
        print(f'Saldo: \tR${saldo:.2f}')
        print("===================")
        print(" ")
    else:
        print("Não foram realizadas movimentações.")
        print("===================")
        print(f'Saldo: \tR${saldo:.2f}')
        print("===================")
        print(" ")
    


def main():

    limite_saques = 3
    saldo = 0
    extrato = "---Extrato bancário---\n"        
    limite = 500
    numero_saques = 1

    while True:
    
        
        opcao = input(menu()).lower().strip()
    

        if opcao == "d":
                        
            valor = float(input("Insira o valor do depósito: "))
            saldo,extrato = depositar(saldo,valor,extrato)
            
        elif opcao == "s":
            
            valor = float(input("Insira o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo=saldo,valor=valor,extrato=extrato,limite=limite,numero_saques=numero_saques,limite_saques=limite_saques)                
              
        elif opcao == "e":
            consultar_extrato(saldo,numero_saques=numero_saques,extrato=extrato)
                
        elif opcao == 'q':
            break

        else:
            print("Opção inválida...")



main()