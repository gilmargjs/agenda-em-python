def menu():
    opcao = input(''' 
=============================================
           PROJETO AGENDA EM PYTHON
MENU:
    
[1]CADASTRAR CONTATO
[2]LISTAR CONTATO
[3]DELETAR CONTATO
[4]BUSCAR CONTATO PELO ID
=============================================
ESCOLHA UMA OPÇÃO ACIMA:
''')

    if opcao == "1":
        cadastrarContato()
    elif opcao == "2":
        listarContato()
    elif opcao == "3":
        deletarContato()
    elif opcao == "4":
        buscarContatoPeloNome()
    elif opcao == "5":
        print(f'Você saiu do Programa....!!!!')

        exit()
    else:
        print(f'Valor Não Está na Lista')


def cadastrarContato():
    idContato = input("Escolha o ID do Contato: ")
    nome = input("Digite o Nome do Conatato: ")
    telefone = input("Digite o Telefone do Contato: ")
    email = input("Digite um Email Valido: ")



    # abrindo ou criando se não existir o arquivo
    # "a" chama o metodo append onde e adicionado na agenda
    # SEPARANDO DADOS ENTRE VIRGULAS PARA SER ABERTO EM EXCEL.
    dados = f'{idContato};{nome};{telefone};{email}\n'
    agenda.write(dados)
    agenda.close()

try:
    print(f'Contato gravado com sucesso !!!!')
except:
    print("ERRO na gravação do contato")


def listarContato():
    agenda = open("agenda.txt", "r")  # abrindo arquivono modo leitura
    # "r" Modo Leitura
    for contato in agenda:
        print(contato)
    agenda.close()


def deletarContato():
    nomeDeletado = input('Digite o Nome Para Ser Deletado')
    agenda = open('agenda.txt','r')
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i]:
            aux2.append(aux[i])
    agenda = open('agenda.txt','w')
    for i in aux2:
        agenda.write(i)
    print(f'contato deletado com sucesso')
    listarContato()

def buscarContatoPeloNome():
    nome = input(f'Digite o nome a ser procurado: ')
    agenda = open("agenda.txt", "r")  # abrindo arquivono modo leitura
    for contato in agenda:  # "r" Modo Leitura
        if nome in contato.split(";")[1]:
            print(contato)

    agenda.close()


def sair():
    exit()


def main():
    menu()


main()
