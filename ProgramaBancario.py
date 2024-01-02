"""
Bancario. Escreva um programa que registre o caixe de um banco. O programa
comeca perguntando se o usuario quer criar uma conta ou fechar o programa.
Se ele escolher fechar o programa escreva uma mensagemd e agradecimento e fecha,
caso contrario ele vai pedir que o usuario selecione um numero com 6 digitos e,
entao, se o numero nao existir no registro do banco, ele ira pedir um valor de
deposito. Depois o banco perguntara se deseja ver o saldo do banco, se sim ele
devera imprimir o balanco geral do banco, senao ele entrara em loop.
"""

contas = []
depositos = []
saldo = 0

def main():
    opcao = bool(int(input("Deseja ver ou criar a conta(1) ou fechar o programa(0): ")))
    while opcao: # = true / 1. Verifica se a variavel tem valor.
        criarConta()
        verSaldo()
        opcao = bool(int(input("Deseja ver ou criar a conta(1) ou fechar o programa(0): ")))
        
def criarConta():
    global contas, depositos, saldo
    num_conta = (int(input("Digite o numero da conta: ")))

    while num_conta in contas:
        print("Conta ja existente, Digite novamente.")
        num_conta = (int(input("Digite o numero da conta: ")))

    contas.append(num_conta)
    deposito = float(input("Digite o valor do primeiro deposito: "))
    while deposito <= 0:
        print("Valor do deposito invalido")
        deposito = float(input("Digite o valor do primeiro deposito: "))
    depositos.append(deposito)
    saldo += deposito

def verSaldo():
    global saldo
    opcao = bool(int(input("Deseja ver o saldo do banco(1 - Sim / 0 - Nao: ")))
    if opcao:
        print("O saldo do banco e R$", saldo)

main()
        

                 
