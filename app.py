intervalo_opcoes_inicial = [1,2,3,4]
restaurantes = []

def tela_inicial():
    #Mensagens da tela inicial
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')
    

def opcoes_inicial():   
    while (1):
        #Pegando dados do usuário
        try:
            escolha_usuario = int(input('\nEscolha uma das opções acima:'))

            if escolha_usuario>=min(intervalo_opcoes_inicial) and escolha_usuario<=max(intervalo_opcoes_inicial):
                break
            else:
                print('\nInforme um valor dentro do intervalo!')
                continue
        except:
            print('\nInforme um valor válido!')
            continue
    return escolha_usuario

def chama_funcoes(escolhido):

    if escolhido==intervalo_opcoes_inicial[0]:
        cadastrar_restaurante()
    else:
        print("Não foi criado ainda")
    
def cadastrar_restaurante():
    nome_restaurante = input("\nInforme o nome do restaurante:")
    categoria_restaurante = input("\nInforme a categoria do restaurante:")
    
    cadastro_restaurante = {'nome':nome_restaurante,'categoria':categoria_restaurante,'ativo':False}
    restaurantes.append(cadastro_restaurante)
    print("Restaurante cadastrado com sucesso!")
    print(restaurantes)


def main():
    tela_inicial()
    escolha_usuario = opcoes_inicial()
    chama_funcoes(escolha_usuario)


#Verificação se a função está dentro do arquivo
if __name__ == '__main__':
    main()