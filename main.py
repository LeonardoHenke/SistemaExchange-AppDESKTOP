import PySimpleGUI as sg
import mods
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


# arquivo de apoio para login e sites
lista_arquivo = open(r"C:\Users\Léo\Desktop\Novo Documento de Texto.txt", "r")
arquivo = lista_arquivo.readlines()


## ---------------------------- Selenium ---------------------------- ##
site_cadastrar = arquivo[3]
site_boletar = arquivo[4]
site_comprar_moeda = arquivo[5]


## ---------------------------- WEB ---------------------------- ##
# baixar o webdriver para a versão certa do navegadoregador escolhido
serv = Service(EdgeChromiumDriverManager().install())


# fazer login no sistema
def login(site):
    # abrindo o site
    navegador.get(site)
    # esperando o menu carregar
    while len(navegador.find_elements(By.ID, "CdAgencia")) == 0:
        sleep(0.5)
    # achando o menu
    menu_login = navegador.find_element(By.ID, "CdAgencia")
    # colocando o menu no select
    agencia_login = Select(menu_login)
    # abrindo o select e achando o valor desejado
    agencia_login.select_by_value("63")
    # preenchendo os campos
    navegador.find_element(By.ID, "CdOperador").send_keys(arquivo[0])
    navegador.find_element(By.ID, "CdSenha").send_keys(arquivo[1])
    # # clicando no ok para logar
    # navegador.find_element(By.ID, "okButton").click()


## ---------------------------- LOOPING PARA LER OS EVENTOS ---------------------------- ##
# definindo as janelas
janela1, janela2, janela3, janela4, janela5 = (mods.janela_ferramentas(), None, None, None, None)

while True:
    # lendo os eventos, os valores e todas as janelas criadas
    janelas, eventos, valores = sg.read_all_windows()
    # condição para fechar
    if eventos == sg.WIN_CLOSED:
        break

    ## ---------------------------- LÓGICA E CÓDIGO ---------------------------- ##
    # --------- janela de ferramentas --------- #
    if janelas == janela1:
        # abrindo a janela cadastrar
        if eventos == "Cadastrar":
            janela1.hide()
            janela2 = mods.janela_cadastro()
            # abrindo a janela boletar
        elif eventos == "Boletar":
            janela1.hide()
            janela3 = mods.janela_boletar()
            # abrindo a janela comprar moeda
        elif eventos == "Comprar Moeda":
            janela1.hide()
            janela4 = mods.janela_comprar_moeda()
            # abrindo a janela consultar saldo
        elif eventos == "Consultar Cadastro":
            janela1.hide()
            janela5 = mods.janela_consult_cadastro()

    # --------- janela de cadastro --------- #
    elif janelas == janela2:
        # voltar pra janela ferramentas
        if eventos == "Voltar":
            janela2.hide()
            janela1.un_hide()
        elif eventos == "Ok":
            # --- abrindo navegador e fazendo login --- #
            #     # dando entrada no navegador
            navegador = webdriver.Edge(service=serv)
            # fazendo login
            login(site_cadastrar)
            # esperando carregar o elemento 'novo'
            while (len(navegador.find_elements(By.XPATH, '//*[@id="RGOPCAO"]/tbody/tr/td[1]/label'))== 0):
                sleep(0.5)
            # clicando na aba novo
            navegador.find_element(By.XPATH, '//*[@id="RGOPCAO"]/tbody/tr/td[1]/label').click()
            # colocando as informações
            # aba cliente
            navegador.find_element(By.ID, "Cdtit1").send_keys(valores["cpf"])
            indicador = Select(navegador.find_element(By.ID, "CdIndicador"))
            indicador.select_by_value(valores["indicador"])
            # aba pessoa física
            navegador.find_element(By.ID, "aba4").click()
            navegador.find_element(By.ID, "Cdrg").send_keys(valores["rg"])
            if valores["sexo"] == "Fem":
                navegador.find_element(By.ID, "Rgsexo_1").click()
            navegador.find_element(By.ID, "Cddatan").send_keys(valores["dt_nasc"])
            navegador.find_element(By.ID, "Cdpai").send_keys(valores["pai"])
            navegador.find_element(By.ID, "Cdmae").send_keys(valores["mae"])
            # aba endereço pais
            navegador.find_element(By.ID, "aba2").click()
            navegador.find_element(By.ID, "Cdcelular").send_keys(valores["celular"])
            navegador.find_element(By.ID, "Cdemail").send_keys(valores["email"])
            navegador.find_element(By.ID, "Cdcep").send_keys(valores["cep"])

    # --------- janela de boletar --------- #
    elif janelas == janela3:
        # voltar pra janela ferramentas
        if eventos == "Voltar":
            janela3.hide()
            janela1.un_hide()
        elif eventos == "Ok":
            # --- abrindo navegador e fazendo login --- #
            #     # dando entrada no navegador
            navegador = webdriver.Edge(service=serv)
            # fazendo login
            login(site_boletar)
            # espernando o mesmo elemento recarregar
            while len(navegador.find_elements(By.ID, "IB_CdConta")) == 0:
                sleep(0.5)
            # clicando no elemento
            navegador.find_element(By.ID, "IB_CdConta").click()
            # espernando o mesmo elemento recarregar
            sleep(1)
            while len(navegador.find_elements(By.ID, "RbVender")) == 0:
                sleep(0.5)
            # selecionando as opções padrões
            navegador.find_element(By.ID, "RbVender").click()
            forma_me = Select(navegador.find_element(By.ID, "Cdformame"))
            forma_me.select_by_value("ESPECIE")
            forma_mn = Select(navegador.find_element(By.ID, "Cdformamn1"))
            forma_mn.select_by_value("TED")
            natureza = Select(navegador.find_element(By.ID, "Cdnatureza"))
            natureza.select_by_value("329990006767")
            conta = Select(navegador.find_element(By.ID, "Cdconta"))
            conta.select_by_value("237 3646   654582")
            # escolhendo moeda e valores
            num_moeda = Select(navegador.find_element(By.ID, "Cdmoeda1"))
            num_moeda.select_by_value(valores["moeda"][:3])
            navegador.find_element(By.ID, "Cdvalorme").send_keys(valores["valor_moeda"])
            navegador.find_element(By.ID, "CdValorrec").send_keys(valores["valor_recebido"])
            navegador.find_element(By.ID, "BCalcularTaxa").click()
            navegador.find_element(By.ID, "BVET").click()
            # abrindo aba de pesquisar cliente
            navegador.find_element(By.ID, "HlCliente").click()
            sleep(1)
            # alterando para mexer no popup que abriu
            navegador.switch_to.window(navegador.window_handles[-1])
            # esperando carregar o elemento
            while len(navegador.find_elements(By.ID, "Cdnomeab")) == 0:
                sleep(0.5)
            # pesquisando o cliente
            if valores["indice"] == "CPF":
                navegador.find_element(By.ID, "Cdnomeab").send_keys(valores["valor_indice"])
                navegador.find_element(By.ID, "Bpesquisar").click()
            else:
                navegador.find_element(By.ID, "Cdnome").send_keys(valores["valor_indice"])
                navegador.find_element(By.ID, "Bpesquisar").click()

    # --------- janela de comprar moeda --------- #
    elif janelas == janela4:
        # voltar pra janela ferramentas
        if eventos == "Voltar":
            janela4.hide()
            janela1.un_hide()
        elif eventos == "Ok":
            # --- abrindo navegador e fazendo login --- #
            #     # dando entrada no navegador
            navegador = webdriver.Edge(service=serv)
            # fazendo login
            login(site_comprar_moeda)
            # esperando carregar o elemento 'novo'
            while len(navegador.find_elements(By.ID, "IB_CdConta")) == 0:
                sleep(0.5)
            # clicando no elemento
            navegador.find_element(By.ID, "IB_CdConta").click()
            # espernando o mesmo elemento recarregar
            sleep(1)
            while len(navegador.find_elements(By.ID, "IB_CdConta")) == 0:
                sleep(0.5)
            # --- colocando os dados --- #
            # colocando a data
            navegador.find_element(By.ID, "CdDataop").clear()
            navegador.find_element(By.ID, "CdDataop").send_keys(valores["data"])
            # selecionando o fluxo de operação
            if valores["data_op"] == "D0":
                navegador.find_element(By.ID, "RgDias_0").click()
            else:
                navegador.find_element(By.ID, "RgDias_1").click()
            # colocando situação em fechado
            status_op = Select(navegador.find_element(By.ID, "CdStatus"))
            status_op.select_by_value("F")
            # colocando a moeda
            num_moeda = Select(navegador.find_element(By.ID, "CdMoeda1"))
            num_moeda.select_by_value(valores["moeda"][:3])
            # colocando o valor comprado
            navegador.find_element(By.ID, "CdValorme").send_keys(valores["valor_moeda"])
            # colocando a taxa
            navegador.find_element(By.ID, "CdTaxaop").send_keys(valores["taxa"])
            # colocando a forma da moeda
            forma_moeda = Select(navegador.find_element(By.ID, "Cdformame2"))
            forma_moeda.select_by_value("ESPECIE")
            # colocando a conta
            if valores["banco"] == "Daycoval":
                conta_banco = Select(navegador.find_element(By.ID, "CdConta"))
                conta_banco.select_by_value("707        0017213877        ")
                # --- colocando o banco --- #
                navegador.find_element(By.ID, "HlCliente").click()
                sleep(1)
                # alterando para mexer no popup que abriu
                navegador.switch_to.window(navegador.window_handles[-1])
                # esperando carregar o elemento
                while len(navegador.find_elements(By.ID, "Cdnomeab")) == 0:
                    sleep(0.5)
                # selecionando o banco
                navegador.find_element(By.ID, "Cdnomeab").send_keys("daycoval")
                navegador.find_element(By.ID, "Bpesquisar").click()

            else:
                conta_banco = Select(navegador.find_element(By.ID, "CdConta"))
                conta_banco.select_by_value("633        0001210757000     ")
                # --- colocando o banco --- #
                navegador.find_element(By.ID, "HlCliente").click()
                sleep(1)
                # alterando para mexer no popup que abriu
                navegador.switch_to.window(navegador.window_handles[-1])
                # esperando carregar o elemento
                while len(navegador.find_elements(By.ID, "Cdnomeab")) == 0:
                    sleep(0.5)
                # selecionando o banco
                navegador.find_element(By.ID, "Cdnomeab").send_keys("rendimento")
                navegador.find_element(By.ID, "Bpesquisar").click()

    # --------- janela de consultar cadastro  --------- #
    elif janelas == janela5:
        # voltar pra janela ferramentas
        if eventos == "Voltar":
            janela5.hide()
            janela1.un_hide()
        elif eventos == "Ok":
            #     # dando entrada no navegador
            navegador = webdriver.Edge(service=serv)
            # fazendo login
            login(site_boletar)
            # esperando carregar o elemento
            while len(navegador.find_elements(By.ID, "HlCliente")) == 0:
                sleep(0.5)
            # abrindo pesquisa
            navegador.find_element(By.ID, "HlCliente").click()
            sleep(1)
            # alterando para mexer no popup que abriu
            navegador.switch_to.window(navegador.window_handles[-1])
            # esperando carregar o elemento
            while len(navegador.find_elements(By.ID, "Cdnomeab")) == 0:
                sleep(0.5)
            # pesquisando o cliente
            if valores["indice"] == "CPF":
                navegador.find_element(By.ID, "Cdnomeab").send_keys(valores["valor_indice"])
            else:
                navegador.find_element(By.ID, "Cdnome").send_keys(valores["valor_indice"])
            navegador.find_element(By.ID, "Bpesquisar").click()


## ---------------------------- FECHAR O PROGRAMA ---------------------------- ##
janela1.close()
