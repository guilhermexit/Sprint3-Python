from time import sleep


#Função pra definir o menu principal
def menu(): 
    menu_fun = ["[1] Cadastrar", "[2] Logar", "[3] Redefinir senha", "[4] Encerrar menu"]
    for i in menu_fun:
        print(i)
    op = int(input("Digite a funcionalidade desejada: "))
    return op


emp_contas = []  #Lista para abrigar os logins/cadastros

def cadastroEmpresa():   #Função para cadastrar empresas
    print("="*50)
    print("OPÇÃO 'CADASTRAR EMPRESA' FOI SELECIONADA")
    sleep(1)
    
    while True:
        emp_nome = input('Digite o nome da empresa: ') 
        emp_contas.append(emp_nome)
        cep_emp = input("Digite o CEP da empresa: ")
        cnpj = input("Digite o CNPJ da empresa: ") 
        while True:
            print(f'Bem vindo(a)', emp_nome,'!')
            sleep(1)
            emp_email = input('Digite o e-mail corporativo da empresa para continuarmos: ')  
            emp_contas.append(emp_email)
            break
        pwd_emp = input("Escolha uma senha para este cadastro: ")
        emp_contas.append(pwd_emp)      
        while True:
            confirm_pwd_emp = input("Confirme sua senha: ")
            if pwd_emp == confirm_pwd_emp:
                sleep(1)
                print("Sua conta corporativa foi criada com sucesso!")
                sleep(1)
                break
            else:
                print("Sua senha está incorreta. Tente novamente.")
        break

cand_contas = []  #Lista para abrigar os logins/cadastros

def cadastroCandidato():   #Função para cadastrar candidatos
    print("="*50)
    print("OPÇÃO 'CADASTRAR CANDIDATO' FOI SELECIONADA")
    sleep(1)
    while True:
        cand_nome = input('Digite seu nome: ')
        cand_contas.append(cand_nome)
        cand_cep = input("Digite seu CEP(Opcional): ")
        cpf = input("Digite seu CPF: ") 
        while True:
            print(f'Bem vindo(a)', cand_nome,'!')
            sleep(1)
            cand_email = input('Digite seu e-mail profissional para continuarmos: ') 
            cand_contas.append(cand_email)
            break
        pwd_cand = input("Escolha uma senha para este cadastro: ")
        cand_contas.append(pwd_cand)       
        while True:
            confirm_pwd_cand = input("Confirme sua senha: ")
            if pwd_cand == confirm_pwd_cand:
                sleep(1)
                print("Sua conta corporativa foi criada com sucesso!")
                sleep(1)
                break
            else:
                print("Sua senha está incorreta. Tente novamente.")
        break



def loginEmpresa():  #Função efetuar o login de empresas
    print("="*50)
    print("OPÇÃO 'LOGAR EMPRESA' FOI SELECIONADA")
    sleep(1)
    while True:
        login_emp = input("Digite o email cadastrado: ")
        if login_emp != emp_contas[1]:
            print("Não foi encontrado nenhum cadastro deste e-mail.")
        else:
            break
    while True:
        pwd_login_emp = input("Digite a senha: ")
        if pwd_login_emp != emp_contas[2]:
            print("Senha incorreta!")
            sleep(1)
        else:
            print("Login efetuado com sucesso.")
            sleep(1)
            break

def loginCandidato():  #Função efetuar o login de candidatos
    print("="*50)
    print("OPÇÃO 'LOGAR CANDIDATO' FOI SELECIONADA")
    sleep(1)
    while True:
        login_cand = input("Digite o email cadastrado: ")
        if login_cand != cand_contas[1]:
            print("Não foi encontrado nenhum cadastro deste e-mail.")
        else:
            break
    while True:
        pwd_login_cand = input("Digite a senha: ")
        if pwd_login_cand != cand_contas[2]:
            print("Senha incorreta!")
            sleep(1)
        else:
            print("Login efetuado com sucesso.")
            sleep(1)
            break

def redefinirSenha(): #Função redefinir senha
    print("="*50)
    print("OPÇÃO 'REDEFINIR SENHA' FOI SELECIONADA")
    sleep(1)
    diff = input("Digite o email registrado: ")
    if diff == emp_contas[1]:
        print("Enviamos uma confirmação em seu e-mail, verifique para poder alterar a senha.")
        sleep(5)
        pwd_login_emp = input("Altere sua senha: ")
        print("Sua senha foi alterada com sucesso.")
        sleep(2)
    elif diff == cand_contas[1]:
        print("Enviamos uma confirmação em seu e-mail, verifique para poder alterar a senha.")
        sleep(5)
        pwd_login_cand = input("Altere sua senha: ")
        print("Sua senha foi alterada com sucesso.")
        sleep(2)
    else: 
        print("Nenhum e-mail registrado neste nome foi encontrado.")
        sleep(1)

def principal():  #Função principal, que abriga todas as outras
    while True:
        opc = menu()
        if opc == 1:
            opCadastro = input("Deseja cadastrar-se como candidato ou empresa?: ") 
            if opCadastro == 'candidato':
                cadastroCandidato()
            elif opCadastro =='empresa':
                cadastroEmpresa()
        if opc == 2:
            opLogin = input("Deseja entrar como candidato ou empresa?: ")
            if opLogin == 'candidato':
                loginCandidato()
            elif opLogin == 'empresa':
                loginEmpresa()
        
        if opc == 3:
            redefinirSenha()

        if opc == 4:
            print("="*50)
            print("Obrigado por utilizar nosso menu! Volte sempre!")
            sleep(3)
            break
      
principal()  #Chamando a função principal
            
