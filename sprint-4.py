from time import sleep
from tokenize import String


#Função pra definir o menu principal
def menu(): 
    menu_fun = ["[1] Cadastrar", "[2] Logar", "[3] Redefinir senha", "[4] Encerrar menu"]
    for i in menu_fun:
        print(i)
    op = int(input("Digite a funcionalidade desejada: "))
    return op



def cadastroEmpresa(emp_contas):   #Função para cadastrar empresas
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



def cadastroCandidato(cand_contas):   #Função para cadastrar candidatos
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
                print("Sua conta foi criada com sucesso!")
                sleep(1)
                break
            else:
                print("Sua senha está incorreta. Tente novamente.")
        break



def loginEmpresa(emp_contas):  #Função efetuar o login de empresas
    print("="*50)
    print("OPÇÃO 'LOGAR EMPRESA' FOI SELECIONADA")
    sleep(1)
    while True:
        login_emp = input("Digite o email cadastrado: ")
        if len(emp_contas) == 0:
            print("Não foi encontrado nenhum cadastro deste e-mail.")
            sleep(1)
            break
        elif login_emp != emp_contas[1]:
            print("Não foi encontrado nenhum cadastro deste e-mail.")
            break
        else:
            break
    while len(emp_contas) != 0:
        pwd_login_emp = input("Digite a senha: ")
        if pwd_login_emp != emp_contas[2]:
            print("Senha incorreta!")
            sleep(1)
        else:
            print("Login efetuado com sucesso.")
            sleep(1)
            break

def loginCandidato(cand_contas):  #Função efetuar o login de candidatos
    print("="*50)
    print("OPÇÃO 'LOGAR CANDIDATO' FOI SELECIONADA")
    sleep(1)
    while True:
        login_cand = input("Digite o email cadastrado: ")
        if len(cand_contas) == 0:
            print("Não foi encontrado nenhum cadastro deste e-mail.")
            sleep(1)
            break
        elif login_cand != cand_contas[1]:
            print("Não foi encontrado nenhum cadastro deste e-mail.")
            break
        else:
            break
    while len(cand_contas) != 0:
        pwd_login_cand = input("Digite a senha: ")
        if pwd_login_cand != cand_contas[2]:
            print("Senha incorreta!")
            sleep(1)
            break
        else:
            print("Login efetuado com sucesso.")
            sleep(1)
            break

def redefinirSenha(emp_contas, cand_contas): #Função redefinir senha
    print("="*50)
    print("OPÇÃO 'REDEFINIR SENHA' FOI SELECIONADA")
    sleep(1)
    while True: 
        redefinir_opc = input("Sua conta é de empresa ou candidato? ")
        if redefinir_opc == 'candidato' and len(cand_contas) != 0: 
            diff_cand = input("Digite o email registrado: ")
            if diff_cand == cand_contas[1]:
                print("Enviamos uma confirmação em seu e-mail, verifique para poder alterar a senha.")
                sleep(5)
                pwd_login_cand = input("Altere sua senha: ")
                cand_contas.insert(2, pwd_login_cand)
                print("Sua senha foi alterada com sucesso.")
                sleep(2)
                break
        elif redefinir_opc == 'empresa' and len(emp_contas) != 0: 
            diff_emp = input("Digite o email registrado: ")
            if diff_emp == emp_contas[1]:
                print("Enviamos uma confirmação em seu e-mail, verifique para poder alterar a senha.")
                sleep(5)
                pwd_login_emp = input("Altere sua senha: ")
                emp_contas.insert(2, pwd_login_emp)
                print("Sua senha foi alterada com sucesso.")
                sleep(2)
                break

        elif len(cand_contas) == 0:
            print("Nenhum e-mail registrado neste nome foi encontrado.")
            sleep(1)
            break

        elif len(emp_contas) == 0:
            print("Nenhum e-mail registrado neste nome foi encontrado.")
            sleep(1)
            break
        else:
            print("Escolha uma opção válida.")
            sleep(1)

        
def opcEscolhida():
    cand_contas = []
    emp_contas = []
    while True:
            opc = menu()
            if opc == 1:
                opCadastro = input("Deseja cadastrar-se como candidato ou empresa?: ").lower()
                if opCadastro == 'candidato':
                    cadastroCandidato(cand_contas)
                elif opCadastro =='empresa':
                    cadastroEmpresa(emp_contas)
            if opc == 2:
                opLogin = input("Deseja entrar como candidato ou empresa?: ").lower()
                if opLogin == 'candidato':
                    loginCandidato(cand_contas)
                elif opLogin == 'empresa':
                    loginEmpresa(emp_contas)
            
            if opc == 3:
                redefinirSenha(emp_contas, cand_contas)
                
            if opc == 4:
                print("="*50)
                print("Obrigado por utilizar nosso menu! Volte sempre!")
                sleep(3)
                break
            if opc >= 5 and String:
                print("="*50)
                print("Selecione uma opção válida!")
                sleep(2)
    return emp_contas, cand_contas


def principal():  #Função principal, que abriga todas as outras
    opcEscolhida()
      

principal()  #Chamando a função principal
            
