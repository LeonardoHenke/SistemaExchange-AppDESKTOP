import PySimpleGUI as sg
from datetime import date


# data de hoje #
dia = date.today().day
mes = date.today().month
if mes < 10:
    mes = f'0{mes}'
ano = date.today().year
data = f'{dia}/{mes}/{ano}'

# moedas
moedas = [
    '150 - AUD - Dólar Australiano',
    "165 - CAD - Dólar Canadense",
    "220 - USD - Dólar Americano",
    "245 - NZD - Dólar da Nova Zelândia",
    "425 - CHF - Franco Suíço",
    "470 - JPY - Iene Japonês",
    "540 - GBP - Libra Esterlina",
    "660 - PEN - Sol Novo",
    "720 - COP - Peso Colombiano",
    "715 - CLP - Peso Chileno",
    "741 - MXN - Peso Mexicano",
    "745 - UYU - Peso Uruguaio",
    "978 - EUR - Euro",
]


## ---------------------------- JANELAS E LAYOUTS ---------------------------- ##

# --------- janela ferramentas --------- # janela1
def janela_ferramentas():
    # criando o layout do programa
    coluna1 = [
        [sg.Button("Cadastrar", button_color="grey", size=(16, 2))],
        [sg.Col([[sg.T(s=17)]])],
        [sg.Button("Comprar Moeda", button_color="grey", size=(16, 2))],
    ]

    coluna2 = [
        [sg.Button("Boletar", button_color="grey", size=(16, 2))],
        [sg.Col([[sg.T()]])],
        [sg.Button("Consultar Cadastro", button_color="grey", size=(16, 2))],
    ]

    layout = [
        [sg.Col([[sg.T()]])],
        [
            sg.T(
                "Selecione a Ferramenta:", font="_ 18", justification="c", expand_x=True
            )
        ],
        [sg.HorizontalSeparator()],
        [sg.Col([[sg.T()]])],
        [sg.Col([[sg.T()]])],
        [sg.Col(coluna1), sg.Col(coluna2)],
        [sg.Col([[sg.T()]])],
        [sg.T(), sg.Button('Acessar Mesa', button_color='grey', size=(35, 2))],
        [sg.Col([[sg.T()]])],
        [sg.Col([[sg.T()]])],
        [
            sg.T("by: Leonardo Henke", s=52, justification="c", font="_ 8"),
        ],
    ]

    # iniciando o programa
    return sg.Window("Ferramentas para Sistema Exchange", layout, finalize=True)


# --------- janela cadastro --------- # janela2
def janela_cadastro():
    # layout
    coluna1 = [
        [sg.T()],
        [sg.T("CPF:")],
        [sg.T("RG:")],
        [sg.T("Data Nasc:")],
        [sg.T("Nome do pai:")],
        [sg.T("Nome da mãe:")],
        [sg.T("CEP:")],
        [sg.T("Celular:")],
        [sg.T("Email:")],
    ]

    coluna2 = [
        [sg.T()],
        [sg.I(key="cpf")],
        [sg.I(key="rg")],
        [sg.I(key="dt_nasc")],
        [sg.I(key="pai")],
        [sg.I(key="mae")],
        [sg.I(key="cep")],
        [sg.I(key="celular")],
        [sg.I(key="email")],
    ]

    layout = [
        [sg.T()],
        [sg.T("Cadastrar", font="_ 18", justification="c", expand_x=True)],
        [sg.HorizontalSeparator()],
        [sg.T()],
        [sg.T("Indicador:", s=17, justification="r"), sg.OptionMenu(default_value="WD CAMBIO", values=["WD CAMBIO", "ANGELA "], key="indicador"), sg.T("Sexo:"), sg.OptionMenu(default_value="Masc", values=["Masc", "Fem"], key="sexo")],
        [sg.Col(coluna1), sg.Col(coluna2)],
        [sg.T()],
        [
            sg.Button("Voltar", button_color="grey", size=(8, 1)),
            sg.T("by: Leonardo Henke", s=50, justification="c", font="_ 8"),
            sg.Button("Ok", button_color="grey", size=(8, 1)),
        ],
    ]

    # CRIANDO A JANELA
    return sg.Window("Ferramentas para Sistema Exchange", layout=layout, finalize=True)


# --------- janela boletar --------- # janela3
def janela_boletar():
    # layout
    coluna1 = [
        [sg.OptionMenu(default_value="CPF", values=["CPF", "Nome"], key="indice")],
        [sg.T("Moeda:")],
        [sg.T("Valor na moeda:")],
        [sg.T("Valor recebido:")],
    ]

    coluna2 = [
        [sg.I(key="valor_indice")],
        [sg.OptionMenu(default_value=moedas[2], values=moedas, key="moeda")],
        [sg.I(key="valor_moeda")],
        [sg.I(key="valor_recebido")],
    ]

    layout = [
        [sg.T()],
        [sg.T("Boletar", font="_ 18", justification="c", expand_x=True)],
        [sg.HorizontalSeparator()],
        [sg.T()],
        [sg.T()],
        [sg.Col(coluna1), sg.Col(coluna2)],
        [sg.T()],
        [
            sg.Button("Voltar", button_color="grey", size=(8, 1)),
            sg.T("by: Leonardo Henke", s=50, justification="c", font="_ 8"),
            sg.Button("Ok", button_color="grey", size=(8, 1)),
        ],
    ]

    # CRIANDO A JANELA
    return sg.Window("Ferramentas para Sistema Exchange", layout=layout, finalize=True)


# --------- janela comprar moeda --------- # janela4
def janela_comprar_moeda():
    # data operação
    data_op = ["D0", "D1"]

    # banco
    bancos = ["Daycoval", "Rendimento"]

    # layout
    coluna1 = [
        [sg.T('Data')],
        [sg.T("Moeda:")],
        [sg.T("Valor na moeda:")],
        [sg.T("Taxa:")],
    ]

    coluna2 = [
        [sg.I(default_text=data, key='data')],
        [sg.OptionMenu(default_value=moedas[2], values=moedas, key="moeda")],
        [sg.I(key="valor_moeda")],
        [sg.I(key="taxa")]
        #   [sg.],
    ]

    layout = [
        [sg.T()],
        [sg.T("Comprar Moeda", font="_ 18", justification="c", expand_x=True)],
        [sg.HorizontalSeparator()],
        [sg.T()],
        [
            sg.T("Operação em:", s=14, justification="r"),
            sg.OptionMenu(default_value=data_op[0], values=data_op, key="data_op"),
            sg.T("Banco:", s=14, justification="r"),
            sg.OptionMenu(default_value=bancos[0], values=bancos, key="banco"),
        ],
        [sg.T()],
        [sg.Col(coluna1), sg.Col(coluna2)],
        [sg.T()],
        [
            sg.Button("Voltar", button_color="grey", size=(8, 1)),
            sg.T("by: Leonardo Henke", s=50, justification="c", font="_ 8"),
            sg.Button("Ok", button_color="grey", size=(8, 1)),
        ],
    ]

    return sg.Window("Ferramentas para Sistema Exchange", layout=layout, finalize=True)


# --------- janela consultar cadastro--------- # janela4
def janela_consult_cadastro():
    layout = [
        [sg.T()],
        [sg.T("Consultar Cadastro", font="_ 18", justification="c", expand_x=True)],
        [sg.HorizontalSeparator()],
        [sg.T()],
        [
            sg.T(s=3),
            sg.OptionMenu(default_value="CPF", values=["CPF", "Nome"], key="indice"),
            sg.I(key="valor_indice"),
        ],
        [sg.T()],
        [
            sg.Button("Voltar", button_color="grey", size=(8, 1)),
            sg.T("by: Leonardo Henke", s=50, justification="c", font="_ 8"),
            sg.Button("Ok", button_color="grey", size=(8, 1)),
        ],
    ]

    return sg.Window("Ferramentas para Sistema Exchange", layout=layout, finalize=True)

