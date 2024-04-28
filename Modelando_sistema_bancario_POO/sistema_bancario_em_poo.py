from datetime import datetime
from abc import ABC, abstractclassmethod, abstractproperty


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = Cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    def sacar(self, valor):
        saldo = self.saldo

        if valor <= 0:
            print("Valor inválido, tente outra vez")
            print(" ")

        elif valor > saldo:

            print("Valor acima do saldo disponível")
            print(" ")

        else:

            self._saldo -= valor
            print("Saque efetuado com sucesso!")
            return True

        return False

    def depositar(self, valor):

        if valor <= 0:

            print("Valor inválido, tente outra vez")
            print(" ")

        else:

            self._saldo += valor
            print(f"Valor depositado com sucesso.")
            return True

        return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques
        if excedeu_limite:
            print("Valor acima do limite diário")
        elif excedeu_saques:
            print("Número de saque diário excedido")
        else:
            return super().sacar(valor)
        return False

    def __str__(self):
        return (
            f"Agência: {self.agencia}\nc/c: {self.numero}\nTitular: {self.cliente.nome}"
        )


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    @property
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M%s"),
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @property
    @abstractproperty
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        transacao_realizada = conta.sacar(self.valor)
        if transacao_realizada:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        self._valor

    def registrar(self, conta):
        transacao_realizada = conta.depositar(self.valor)
        if transacao_realizada:
            conta.historico.adicionar_transacao(self)
