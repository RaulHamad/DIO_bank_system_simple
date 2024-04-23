def menu():

    menu = "=====Sistema bancário=====\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[cl] Cadastrar Cliente\n[l] Listar Cliente\n[cc] Criar Conta\n[lc] Listar Contas\n[q] Sair\nSelecione uma opção: "
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
      
        extrato += f'Saque R${valor:.2f}\n'
        saldo -= valor
        numero_saques += 1
        print("Saque efetuado com sucesso!")
        
    return saldo, extrato ,numero_saques

    
def consultar_extrato(saldo,/,*,numero_saques,extrato):
    
    print(extrato)
    print("===================")
    print(f'Saldo: \tR${saldo:.2f}')
    print("===================")
    print(" ")


def criar_cliente(usuarios):

    cpf = int(input("digite seu cpf (apenas números): "))
    cliente = filtrar_cliente(cpf,usuarios)

    if cliente:
        print("===== Usuário já cadastrado =====")
        print(" ")
        return
    else:
        nome = input("Digite seu nome completo: ")
        data_nascimento = input("Digite sua data de nascimento (dd/mm/aa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({"nome":nome, "data_nascimento": data_nascimento,"cpf":cpf,"endereço":endereco})



def filtrar_cliente(cpf,usuarios):
    
    for cliente in usuarios:
        if cliente["cpf"] == cpf:
            usuario_filtrado = [cliente]
            return usuario_filtrado[0]
        else:
            None 


def listar_clientes(usuarios):
    
    print("=== Lista de clientes ===")
    print(" ")
    for cliente in usuarios:
        print(cliente)
    print(" ")

    
def criar_conta(agencia, numero_da_conta, usuarios):

    cpf = int(input("Informe o CPF do cliente: "))
    cliente = filtrar_cliente(cpf,usuarios)
    
    if cliente:
        print("===== Conta criada com sucesso! =====")
        return {"agencia": agencia, "numero_conta": numero_da_conta, "usuario": cliente}
    
    print("===== Usuário não encontrado! =====")

def listar_contas(contas):
    print("=== Lista de contas ===")
    print(" ")
    for cliente in contas:
        print(f'Agencia: {cliente["agencia"]}')
        print(f'Conta: {cliente["numero_conta"]}')
        print(f'Cliente: {cliente["usuario"]["nome"]}')
        print("===")
    print(" ")

def main():

    limite_saques = 3
    saldo = 0
    extrato = "---Extrato bancário---\n"        
    limite = 500
    numero_saques = 1
    usuarios = list()
    contas = []
    agencia = "0001"

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
                
        elif opcao == 'cl':
            criar_cliente(usuarios)

        elif opcao == 'l':
            listar_clientes(usuarios)

        elif opcao == 'cc':
            numero_da_conta = len(contas) + 1
            conta = criar_conta(agencia,numero_da_conta,usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'q':
            break

        elif opcao == 'lc':
            listar_contas(contas)

        else:
            print("Opção inválida...")



main()