import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import oficial_func as of

def importa_df(caminho):
    df = pd.read_csv(caminho + "feed.csv")
    print(df.dtypes)
    print(df.describe)

    # 1) Renomeando as colunas
    df.rename(columns={'created_at': 'Data', 'field1': 'Ax', 'field2': 'Ay', 'field3': 'Az',
                       'field4': 'Temperatura', 'field5': 'Umidade1', 'field6': 'Umidade2',
                       'field7': 'Umidade3'}, inplace=True)

    # 2) Transformar data em DateTime
    df['Data'] = pd.to_datetime(df['Data'])
    times_index = pd.Index(df['Data'])
    times_index_brasilia = times_index.tz_convert('America/Sao_Paulo')
    times_index_brasilia
    df_data = df.set_index(times_index_brasilia)

    return df_data

def graficos_df_ACeT(df_data): # GRÁFICO 1 (3 ACELERAÇÕES + TEMPERATURA)

    #"plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"

    grafico1 = go.Figure()
    grafico1 = make_subplots(specs=[[{"secondary_y": True}]])
    grafico1.add_trace(go.Scatter(x=df_data.index, y=df_data['Ax'], mode='lines', name='Aceleração x'))
    grafico1.add_trace(go.Scatter(x=df_data.index, y=df_data['Ay'], mode='lines', name='Aceleração y'))
    grafico1.add_trace(go.Scatter(x=df_data.index, y=df_data['Az'], mode='lines', name='Aceleração z'))
    grafico1.add_trace(go.Scatter(x=df_data.index, y=df_data['Temperatura'], mode='lines',
                                  name='Temperatura'), secondary_y=True)

    # Set x-axis title
    grafico1.update_xaxes(title_text="Data (local - Niterói)")

    # Set y-axes titles
    grafico1.update_yaxes(title_text="Acelerações", secondary_y=False)
    grafico1.update_yaxes(title_text="Temperatura", secondary_y=True)

    # Template do gráfico
    # https://plotly.com/python/templates/
    grafico1.update_layout(template='simple_white', title="Acelerações em x, y, z e Temperatura",
                           legend=dict(yanchor="top", y=1.2, xanchor="right", x=1.4))

    return grafico1

def graficos_df_U123(df_data): # GRÁFICO 2 (3 UMIDADES)
    grafico2 = go.Figure()
    grafico2.add_trace(
        go.Scatter(x=df_data.index, y=df_data['Umidade1'], mode='lines', name='Umidade - profundidade 1'))
    grafico2.add_trace(
        go.Scatter(x=df_data.index, y=df_data['Umidade2'], mode='lines', name='Umidade - profundidade 2'))
    grafico2.add_trace(
        go.Scatter(x=df_data.index, y=df_data['Umidade3'], mode='lines', name='Umidade - profundidade 3'))

    # Set x-axis title
    grafico2.update_xaxes(title_text="Data (local - Niterói)")

    # Set y-axes titles
    grafico2.update_yaxes(title_text="Umidades")

    # Template do gráfico
    # https://plotly.com/python/templates/
    grafico2.update_layout(template='simple_white', title="Umidades",
                           legend=dict(yanchor="top", y=1.2, xanchor="right", x=1.4))

    return grafico2

def grafico_df_mapa(alerta_df):
    #IMPORTA OS DADOS
    df_UFF = of.importa_df("https://thingspeak.com/channels/1670099/")
    df_Jurujuba_L1 = of.importa_df("https://thingspeak.com/channels/609692/")
    df_Jurujuba_L2 = of.importa_df("https://thingspeak.com/channels/1962134/")
    df_Jurujuba_L3 = of.importa_df("https://thingspeak.com/channels/1962136/")

    #Executa os alarmes
    #Definir Alarmes
    # HEX COLORS
    # https://htmlcolorcodes.com
    teste = "#9C1FBD"
    teste1 = "#f70d1a"
    teste2 = "#EEEE0A"
    teste3 = "#3DEC0A"
    #Alarmes UFF
    # Alarme ACeT 
    # Alarme U123
    alarmeUFF_U123 = of.alarme_U123(df_UFF, 30, 10, -10, "Umidade3")

    #Alarmes Jurujuba L1
    # Alarme ACeT 
    # Alarme U123
    alarmeJL1_U123 = of.alarme_U123(df_Jurujuba_L1, 30, 10, -10, "Umidade3")

    #Alarmes Jurujuba L2
    # Alarme ACeT 
    # Alarme U123
    alarmeJL2_U123 = of.alarme_U123(df_Jurujuba_L2, 30, 10, -10, "Umidade3")

    #Alarmes Jurujuba L3
    # Alarme ACeT 
    # Alarme U123
    alarmeJL3_U123 = of.alarme_U123(df_Jurujuba_L3, 30, 10, -10, "Umidade3")

    fig_mapa = px.scatter_mapbox(alerta_df, lat="latitude", lon="longitude", zoom=(int(11)),
                                 size_max=(int(12)), size=[6, 6, 6, 6, 6, 6, 6, 6],
                                 center={"lat": -22.898979, "lon": -43.039131},
                                 color="Sinais de Alerta", opacity=[1, 0.7, 1, 0.7, 1, 0.7, 1, 0.7],
                                 #       text=["UFF","Jurujuba 1", "Jurujuba 2"],
                                 color_discrete_map={"UFF ACeT": teste, "UFF U123": alarmeUFF_U123,
                                                     "Jurujuba1 ACeT": teste2, "Jurujuba1 U123": alarmeJL1_U123,
                                                     "Jurujuba2 ACeT": teste1, "Jurujuba2 U123": alarmeJL2_U123,
                                                     "Jurujuba3 ACeT": teste, "Jurujuba U123": alarmeJL3_U123})

    fig_mapa.update_layout(mapbox_style="stamen-terrain")

    return fig_mapa

#DEFINIR AS FUNÇÕES DOS ALARMES
def alarme_U123(df_UFF, n1_u3, n2_u3, diferença_u3, col_u3):
    #df_UFF -> DataFrame tratado na primeira função
    #n1_u3 -> df dos Ultimos "n1_u3" valores de Umidade3 (maior espaçamento)
    #n2_u3 -> df dos Ultimos "n2_u3" valores de Umidade3 (menor espaçamento)
    #diferença_u3 -> diferença a ser considerada nas médias para o encremento do alarme
    #col_u3 -> corresponde a coluna de "Umidade3" (pode ser que posteriormente algo mude aqui ou em todo resto)

    #Pega os valores dos alarmes dos últimos valores de dados
    ultima_info = df_UFF.tail(1)
    ultima_info.loc[ultima_info[col_u3] < 50, "cor"] = "#9C1FBD" #roxo
    ultima_info.loc[((ultima_info[col_u3] >= 50) & (ultima_info[col_u3] <= 100)), "cor"] = "#f70d1a" #vermelho
    ultima_info.loc[((ultima_info[col_u3] > 100) & (ultima_info[col_u3] <= 200)), "cor"] = "#EEEE0A" #amarelo
    ultima_info.loc[ultima_info[col_u3] > 200, "cor"] = "#3DEC0A" #verde

    #Pega a cor correspondente ao alarme de acordo com os valores avaliados a cima.

    valor = ultima_info.iloc[0]["cor"]

    #Calcula as médias entre n1_u3 e n2_u3
    media_n1 = df_UFF[col_u3].tail(n1_u3).mean()
    media_n2 = df_UFF[col_u3].tail(n2_u3).mean()

    #Se a subtração das médias derem negativo significa que o valor de U3 está diminuindo e logo está piorando a situação
    if ((media_n2 - media_n1) <= diferença_u3):
        if valor == "#3DEC0A": #Quando verde ele vai para amarelo
            valor = "#EEEE0A"
        elif valor == "#EEEE0A": #Quando amarelo vai para vermelho
            valor = "#f70d1a"
        elif valor == "#f70d1a": #Quando vermelho vai para roxo
            valor = "#9C1FBD"
        else:
            valor = "#9C1FBD"
    
    return valor
