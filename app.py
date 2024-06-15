import textwrap
s = "Sistema Bancario"
print(s.center(50, '*'))
     
  
def menu(usuarios,contas):
    menu = ''
    if not usuarios:
        menu += """           
            [nu]  Novo Usuário
            [q]   Sair
            =>    """
    elif not contas:
        menu += """
            [nc]  Nova Conta
            [nu]  Novo Usuário
            [lc]  Listar Contas
            [lu]  Listar Usarios
            [q]   Sair
        """
    else : 
        menu = """
            [d]   Depositar
            [s]   Sacar
            [e]   Extrato
            [nc]  Nova Conta
            [lc]  Listar Contas
            [nu]  Novo Usuário
            [lu]  Listar Usarios
            [q]   Sair
            => 
        """
    return input(textwrap.dedent(menu))
   

def depositar(saldo, valor, extrato , /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        return (saldo, extrato)            
    else:
        print('Operação Falhou! O valor informado é inválido')
        
        
def sacar(*,saldo,valor,extrato,limite, numero_sareus, limite_saques):
    return saldo, extrato 
 
def exibir_extrato(saldo,/, *, extrato):
    return 0

def cadastrar_usuario(usuarios):
    
    nome = input('Digite o nome do usuario :')
    data_de_nascimento = input('digite a data de nascimento :')
    cpf = input('Digite o CPF do usuário: ')
    endereco = input('Digite o Endereço do usuário: ')
    usuarios.append([nome,data_de_nascimento,cpf,endereco])
    print('fim do cadastro de usuário'.center(50,'*'))
    return usuarios

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_cota(agencia , numero_conta, usuario):
    agencia = '0001'
    numero_da_conta = 1
    usuario_cpf = 'xxxx'
    return 0

def filtrar_conta(numero_conta, lista_conta):
    conta_filtradas = [conta for lista_conta in conta if  conta == numero_conta]
    return conta_filtrada

def main():
    
    AGENCIA = '0001'
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    
    usuarios = []
    contas = []

    while True:
        inicio = 'Inicio menu'.center(50,'=')
        fim = 'Fim menu'.center(50,'=')
        print(inicio)
        opcao = menu(usuarios,contas)
      #  print(fim)
        if opcao == 'd':
            valor = float(input("Informe o valor do depósito: "))
            
            saldo , extrato = depositar(saldo, valor , extrato)
            
        
        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))
            excedeu_saldo = valor > saldo
            
            excedeu_limite = valor > limite
            
            excedeu_saques = numero_saques >= LIMITE_SAQUES 
            
            if excedeu_saldo:
                print('Operação falhou! Você não tem saldo suficiente.')
                
            elif excedeu_limite:
                print('Operação falhou! O valor do saque excede o limite')
            elif excedeu_saques:
                print('Operação falhou! Número máximo de saques excedido')
            
            elif valor > 0:
                saldo -= valor
                extrato += f'Saque: R$ {valor:.2f}\n'
                numero_saques += 1
                
            else:
                print("Operação falhou! Ovalor informado é inválido.")
        
        elif opcao == 'e':
            print('\n ')
            print('EXTRATO'.center(50,'='))
            print("Não foram realizadas movimentações" if not extrato else extrato)
            print('\n')
            print(f'Saldo: R$ {saldo:.2f}')
            print(''.center(50,'='))
        elif opcao == 'nu':
            string = 'Cadastrar usuarios'
            print(string.center(50,'='))
            cadastrar_usuario(usuarios)                
        elif opcao == 'q':
            break

       
        else:
            print('Operação inválida, por favor selecione novamente a operação desejada.')
        
main()