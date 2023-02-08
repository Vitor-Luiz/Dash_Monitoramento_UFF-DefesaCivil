from dash import html, dcc, callback, Input, Output
import dash_daq as daq
from dash.dependencies import Input, Output
import plotly.io as pio
import dash
import oficial_func as of

df_UFF = of.importa_df("https://thingspeak.com/channels/1670099/")
df_Jurujuba_L1 = of.importa_df("https://thingspeak.com/channels/609692/")
df_Jurujuba_L2 = of.importa_df("https://thingspeak.com/channels/1962134/")
df_Jurujuba_L3 = of.importa_df("https://thingspeak.com/channels/1962136/")

#Definir Alarmes
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

# HEX COLORS
# https://htmlcolorcodes.com
teste = "#9C1FBD"
teste1 = "#f70d1a"
teste2 = "#EEEE0A"
teste3 = "#3DEC0A"
x = "ALARME"

#Gráficos
pio.templates
#Gráficos UFF
figuraUFF_ACeT = of.graficos_df_ACeT(df_UFF)
figuraUFF_U123 = of.graficos_df_U123(df_UFF)
#Gráficos Jurujuba L1
figuraJL1_ACeT = of.graficos_df_ACeT(df_Jurujuba_L1)
figuraJL1_U123 = of.graficos_df_U123(df_Jurujuba_L1)
#Gráficos Jurujuba L2
figuraJL2_ACeT = of.graficos_df_ACeT(df_Jurujuba_L2)
figuraJL2_U123 = of.graficos_df_U123(df_Jurujuba_L2)
#Gráficos Jurujuba L3
figuraJL3_ACeT = of.graficos_df_ACeT(df_Jurujuba_L3)
figuraJL3_U123 = of.graficos_df_U123(df_Jurujuba_L3)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
dash.register_page(__name__, external_stylesheets=external_stylesheets)

layout = html.Div([
    html.Div([
        html.Div([
            html.H3('UFF_ACeT', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='UFF_ACeT', figure=figuraUFF_ACeT, className="teste"),
            html.H2(children=[daq.Indicator(id='alarme_UFF_ACeT', label=x, value=True, size=40, color=teste1)],
                    style={"color": teste1, "text-align": "center"}),
            dcc.Interval(id='interval-component_UFF_ACeT', interval=1 * 180000, n_intervals=0)
        ], className='six columns'),

        html.Div([
            html.H3('UFF_U123', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='UFF_U123', figure=figuraUFF_U123, className='teste'),
            html.H2(children=[daq.Indicator(id='alarme_UFF_U123', label=x, value=True, size=40, color=alarmeUFF_U123)],
                    style={"color": alarmeUFF_U123, "text-align": "center"}),
            dcc.Interval(id='interval-component_UFF_U123', interval=1 * 180000, n_intervals=0)
        ], className="six columns"),
    ], className='row'),

    html.Div([
        html.Div([
            html.H3('JurujubaL1_ACeT', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='JurujubaL1_ACeT', figure=figuraJL1_ACeT, className="teste"),
            html.H2(children=[daq.Indicator(id='alarme_JurujubaL1_ACeT', label=x, value=True, size=40, color=teste1)],
                    style={"color": teste1, "text-align": "center"}),
            dcc.Interval(id='interval-component_JurujubaL1_ACeT', interval=1 * 180000, n_intervals=0)
        ], className='six columns'),

        html.Div([
            html.H3('JurujubaL1_U123', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='JurujubaL1_U123', figure=figuraJL1_U123, className='teste'),
            html.H2(children=[daq.Indicator(id='alarme_JurujubaL1_U123', label=x, value=True, size=40, color=alarmeJL1_U123)],
                    style={"color": alarmeJL1_U123, "text-align": "center"}),
            dcc.Interval(id='interval-component_JurujubaL1_U123', interval=1 * 180000, n_intervals=0)
        ], className="six columns"),
    ], className='row'),

    html.Div([
        html.Div([
            html.H3('JurujubaL2_ACeT', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='JurujubaL2_ACeT', figure=figuraJL2_ACeT, className="teste"),
            html.H2(children=[daq.Indicator(id='alarme_JurujubaL2_ACeT', label=x, value=True, size=40, color=teste1)],
                    style={"color": teste1, "text-align": "center"}),
            dcc.Interval(id='interval-component_JurujubaL2_ACeT', interval=1 * 180000, n_intervals=0)
        ], className='six columns'),

        html.Div([
            html.H3('JurujubaL2_U123', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='JurujubaL2_U123', figure=figuraJL2_U123, className='teste'),
            html.H2(children=[daq.Indicator(id='alarme_JurujubaL2_U123', label=x, value=True, size=40, color=alarmeJL2_U123)],
                    style={"color": alarmeJL2_U123, "text-align": "center"}),
            dcc.Interval(id='interval-component_JurujubaL2_U123', interval=1 * 180000, n_intervals=0)
        ], className="six columns"),
    ], className='row'),

    html.Div([
        html.Div([
            html.H3('JurujubaL3_ACeT', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='JurujubaL3_ACeT', figure=figuraJL3_ACeT, className="teste"),
            html.H2(children=[daq.Indicator(id='alarme_JurujubaL3_ACeT', label=x, value=True, size=40, color=teste1)],
                    style={"color": teste1, "text-align": "center"}),
            dcc.Interval(id='interval-component_JurujubaL3_ACeT', interval=1 * 180000, n_intervals=0)
        ], className='six columns'),

        html.Div([
            html.H3('JurujubaL3_U123', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='JurujubaL3_U123', figure=figuraJL3_U123, className='teste'),
            html.H2(children=[daq.Indicator(id='alarme_JurujubaL3_U123', label=x, value=True, size=40, color=alarmeJL3_U123)],
                    style={"color": alarmeJL3_U123, "text-align": "center"}),
            dcc.Interval(id='interval-component_JurujubaL3_U123', interval=1 * 180000, n_intervals=0)
        ], className="six columns"),
    ], className='row')

])

#UFF____________________________________________________________________________________________________________________
# (1) ATUALIZAÇÃO DO GRÁFICO ACeT UFF
@callback(Output('UFF_ACeT', 'figure'),
          Input('interval-component_UFF_ACeT', 'n_intervals'))
def update_xyz_temperatura(n):
    df_UFF = of.importa_df("https://thingspeak.com/channels/1670099/")
    figuraUFF_ACeT = of.graficos_df_ACeT(df_UFF)
    return figuraUFF_ACeT

# (2) ATUALIZAÇÃO DO sinal de alarme de ACeT UFF
@callback(Output('alarme_UFF_ACeT', 'color'),
          Input('interval-component_UFF_ACeT', 'n_intervals'))
def funcao_alarme1(n):
    df_UFF = of.importa_df("https://thingspeak.com/channels/1670099/")
    teste = "#9C1FBD"
    teste1 = "#f70d1a"
    teste2 = "#EEEE0A"
    teste3 = "#3DEC0A"
    return teste

# (3) ATUALIZAÇÃO DO do gráfico U123 UFF
@callback(Output('UFF_U123', 'figure'),
          Input('interval-component_UFF_U123', 'n_intervals'))
def update_Umidades(n):
    df_UFF = of.importa_df("https://thingspeak.com/channels/1670099/")
    figuraUFF_U123 = of.graficos_df_U123(df_UFF)
    return figuraUFF_U123

# (4) ATUALIZAÇÃO DO sinal de alarme de U123 UFF
@callback(Output('alarme_UFF_U123', 'color'),
          Input('interval-component_UFF_U123', 'n_intervals'))
def funcao_alarme2(n):
    df_UFF = of.importa_df("https://thingspeak.com/channels/1670099/")
    alarmeUFF_U123 = of.alarme_U123(df_UFF, 30, 10, -10, "Umidade3")
    return alarmeUFF_U123

#JURUJUBA 1_____________________________________________________________________________________________________________

# (5) ATUALIZAÇÃO DO GRÁFICO ACeT JURUJUBA1
@callback(Output('JurujubaL1_ACeT', 'figure'),
          Input('interval-component_JurujubaL1_ACeT', 'n_intervals'))
def update_xyz_temperatura2(n):
    df_Jurujuba_L1 = of.importa_df("https://thingspeak.com/channels/609692/")
    figuraJL1_ACeT = of.graficos_df_ACeT(df_Jurujuba_L1)
    return figuraJL1_ACeT

# (6) ATUALIZAÇÃO do sinal de alarme de ACeT JURUJUBA1
@callback(Output('alarme_JurujubaL1_ACeT', 'color'),
          Input('interval-component_JurujubaL1_ACeT', 'n_intervals'))
def funcao_alarme3(n):
    df_Jurujuba_L1 = of.importa_df("https://thingspeak.com/channels/609692/")
    teste = "#9C1FBD"
    teste1 = "#f70d1a"
    teste2 = "#EEEE0A"
    teste3 = "#3DEC0A"
    return teste

# (7) ATUALIZAÇÃO DO do gráfico U123 JURUJUBA1
@callback(Output('JurujubaL1_U123', 'figure'),
          Input('interval-component_JurujubaL1_U123', 'n_intervals'))
def update_Umidades2(n):
    df_Jurujuba_L1 = of.importa_df("https://thingspeak.com/channels/609692/")
    figuraJL1_U123 = of.graficos_df_U123(df_Jurujuba_L1)
    return figuraJL1_U123

# (8) ATUALIZAÇÃO DO sinal de alarme de U123 Jurujuba1
@callback(Output('alarme_JurujubaL1_U123', 'color'),
          Input('interval-component_JurujubaL1_U123', 'n_intervals'))
def funcao_alarme4(n):
    df_Jurujuba_L1 = of.importa_df("https://thingspeak.com/channels/609692/")
    alarmeJL1_U123 = of.alarme_U123(df_Jurujuba_L1, 30, 10, -10, "Umidade3")
    return alarmeJL1_U123

#JURUJUBA 2_____________________________________________________________________________________________________________

# (9) ATUALIZAÇÃO DO GRÁFICO ACeT JURUJUBA2
@callback(Output('JurujubaL2_ACeT', 'figure'),
          Input('interval-component_JurujubaL2_ACeT', 'n_intervals'))
def update_xyz_temperatura3(n):
    df_Jurujuba_L2 = of.importa_df("https://thingspeak.com/channels/1962134/")
    figuraJL2_ACeT = of.graficos_df_ACeT(df_Jurujuba_L2)
    return figuraJL2_ACeT

# (10) ATUALIZAÇÃO do sinal de alarme de ACeT JURUJUBA2
@callback(Output('alarme_JurujubaL2_ACeT', 'color'),
          Input('interval-component_JurujubaL2_ACeT', 'n_intervals'))
def funcao_alarme5(n):
    df_Jurujuba_L2 = of.importa_df("https://thingspeak.com/channels/1962134/")
    teste = "#9C1FBD"
    teste1 = "#f70d1a"
    teste2 = "#EEEE0A"
    teste3 = "#3DEC0A"
    return teste

# (11) ATUALIZAÇÃO DO do gráfico U123 JURUJUBA2
@callback(Output('JurujubaL2_U123', 'figure'),
          Input('interval-component_JurujubaL2_U123', 'n_intervals'))
def update_Umidades3(n):
    df_Jurujuba_L2 = of.importa_df("https://thingspeak.com/channels/1962134/")
    figuraJL2_U123 = of.graficos_df_U123(df_Jurujuba_L2)
    return figuraJL2_U123

# (12) ATUALIZAÇÃO DO sinal de alarme de U123 JURUJUBA2
@callback(Output('alarme_JurujubaL2_U123', 'color'),
          Input('interval-component_JurujubaL2_U123', 'n_intervals'))
def funcao_alarme6(n):
    df_Jurujuba_L2 = of.importa_df("https://thingspeak.com/channels/1962134/")
    alarmeJL2_U123 = of.alarme_U123(df_Jurujuba_L2, 30, 10, -10, "Umidade3")
    return alarmeJL2_U123

#JURUJUBA 3_____________________________________________________________________________________________________________
# (13) ATUALIZAÇÃO DO GRÁFICO ACeT JURUJUBA3
@callback(Output('JurujubaL3_ACeT', 'figure'),
          Input('interval-component_JurujubaL3_ACeT', 'n_intervals'))
def update_xyz_temperatura4(n):
    df_Jurujuba_L3 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraJL3_ACeT = of.graficos_df_ACeT(df_Jurujuba_L3)
    return figuraJL3_ACeT

# (14) ATUALIZAÇÃO do sinal de alarme de ACeT JURUJUBA3
@callback(Output('alarme_JurujubaL3_ACeT', 'color'),
          Input('interval-component_JurujubaL3_ACeT', 'n_intervals'))
def funcao_alarme7(n):
    df_Jurujuba_L3 = of.importa_df("https://thingspeak.com/channels/1962136/")
    teste = "#9C1FBD"
    teste1 = "#f70d1a"
    teste2 = "#EEEE0A"
    teste3 = "#3DEC0A"
    return teste

# (15) ATUALIZAÇÃO DO do gráfico U123 JURUJUBA3
@callback(Output('JurujubaL3_U123', 'figure'),
          Input('interval-component_JurujubaL3_U123', 'n_intervals'))
def update_Umidades4(n):
    df_Jurujuba_L3 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraJL3_U123 = of.graficos_df_U123(df_Jurujuba_L3)
    return figuraJL3_U123

# (16) ATUALIZAÇÃO DO sinal de alarme de U123 JURUJUBA3
@callback(Output('alarme_JurujubaL3_U123', 'color'),
          Input('interval-component_JurujubaL3_U123', 'n_intervals'))
def funcao_alarme8(n):
    df_Jurujuba_L3 = of.importa_df("https://thingspeak.com/channels/1962136/")
    alarmeJL3_U123 = of.alarme_U123(df_Jurujuba_L3, 30, 10, -10, "Umidade3")
    return alarmeJL3_U123

#FIM____________________________________________________________________________________________________________________

#!
#layout.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
#!