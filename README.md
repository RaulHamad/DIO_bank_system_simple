<h1>
    <a href="https://www.dio.me/">
     <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png"></a>
    <span> Desafio criando um sistema bancário </span>
</h1>

## Objetivo 🎯
Criar um sistema bancário com as operações:depositar, sacar, extrato

## Desafio
Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem python.
Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

### Depósito
Deve ser possível depositar valores positivos para minha conta bancária. A versão 1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária.
Todos os depósitos devem ser armazenados em uam variável e exibidos na operação de extrato.

### Saque
O sistema deve permitir realizar 3 saques diários com limite de no máximo R$500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.

### Extrato
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R$xxx.xx
