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
#Mais 10 locais de sensores
df_Local_1 = of.importa_df("https://thingspeak.com/channels/1962136/")
df_Local_2 = of.importa_df("https://thingspeak.com/channels/1962136/")
df_Local_3 = of.importa_df("https://thingspeak.com/channels/1962136/")
df_Local_4 = of.importa_df("https://thingspeak.com/channels/1962136/")
df_Local_5 = of.importa_df("https://thingspeak.com/channels/1962136/")
df_Local_6 = of.importa_df("https://thingspeak.com/channels/1962136/")
df_Local_7 = of.importa_df("https://thingspeak.com/channels/1962136/")
df_Local_8 = of.importa_df("https://thingspeak.com/channels/1962136/")
df_Local_9 = of.importa_df("https://thingspeak.com/channels/1962136/")
df_Local_10 = of.importa_df("https://thingspeak.com/channels/1962136/")

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

#Alarmes Local1
# Alarme ACeT 
# Alarme U123
alarmeL1_U123 = of.alarme_U123(df_Local_1, 30, 10, -6, "Umidade3")

#Alarmes Local2
# Alarme ACeT 
# Alarme U123
alarmeL2_U123 = of.alarme_U123(df_Local_2, 30, 10, -6, "Umidade3")

#Alarmes Local3
# Alarme ACeT 
# Alarme U123
alarmeL3_U123 = of.alarme_U123(df_Local_3, 30, 10, -6, "Umidade3")

#Alarmes Local4
# Alarme ACeT 
# Alarme U123
alarmeL4_U123 = of.alarme_U123(df_Local_4, 30, 10, -6, "Umidade3")

#Alarmes Local5
# Alarme ACeT 
# Alarme U123
alarmeL5_U123 = of.alarme_U123(df_Local_5, 30, 10, -6, "Umidade3")

#Alarmes Local6
# Alarme ACeT 
# Alarme U123
alarmeL6_U123 = of.alarme_U123(df_Local_6, 30, 10, -6, "Umidade3")

#Alarmes Local7
# Alarme ACeT 
# Alarme U123
alarmeL7_U123 = of.alarme_U123(df_Local_7, 30, 10, -6, "Umidade3")

#Alarmes Local8
# Alarme ACeT 
# Alarme U123
alarmeL8_U123 = of.alarme_U123(df_Local_8, 30, 10, -6, "Umidade3")

#Alarmes Local9
# Alarme ACeT 
# Alarme U123
alarmeL9_U123 = of.alarme_U123(df_Local_9, 30, 10, -6, "Umidade3")

#Alarmes Local10
# Alarme ACeT 
# Alarme U123
alarmeL10_U123 = of.alarme_U123(df_Local_10, 30, 10, -6, "Umidade3")

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
#Gráficos Local 1
figuraL1_ACeT = of.graficos_df_ACeT(df_Local_1)
figuraL1_U123 = of.graficos_df_U123(df_Local_1)
#Gráficos Local 2
figuraL2_ACeT = of.graficos_df_ACeT(df_Local_2)
figuraL2_U123 = of.graficos_df_U123(df_Local_2)
#Gráficos Local 3
figuraL3_ACeT = of.graficos_df_ACeT(df_Local_3)
figuraL3_U123 = of.graficos_df_U123(df_Local_3)
#Gráficos Local 4
figuraL4_ACeT = of.graficos_df_ACeT(df_Local_4)
figuraL4_U123 = of.graficos_df_U123(df_Local_4)
#Gráficos Local 5
figuraL5_ACeT = of.graficos_df_ACeT(df_Local_5)
figuraL5_U123 = of.graficos_df_U123(df_Local_5)
#Gráficos Local 6
figuraL6_ACeT = of.graficos_df_ACeT(df_Local_6)
figuraL6_U123 = of.graficos_df_U123(df_Local_6)
#Gráficos Local 7
figuraL7_ACeT = of.graficos_df_ACeT(df_Local_7)
figuraL7_U123 = of.graficos_df_U123(df_Local_7)
#Gráficos Local 8
figuraL8_ACeT = of.graficos_df_ACeT(df_Local_8)
figuraL8_U123 = of.graficos_df_U123(df_Local_8)
#Gráficos Local 9
figuraL9_ACeT = of.graficos_df_ACeT(df_Local_9)
figuraL9_U123 = of.graficos_df_U123(df_Local_9)
#Gráficos Local 10
figuraL10_ACeT = of.graficos_df_ACeT(df_Local_10)
figuraL10_U123 = of.graficos_df_U123(df_Local_10)

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
    ], className='row'),

    html.Div([
        html.Div([
            html.H3('Local1_ACeT', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local1_ACeT', figure=figuraL1_ACeT, className="teste"),
            html.H2(children=[daq.Indicator(id='alarme_Local1_ACeT', label=x, value=True, size=40, color=teste1)],
                    style={"color": teste1, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local1_ACeT', interval=1 * 180000, n_intervals=0)
        ], className='six columns'),

        html.Div([
            html.H3('Local1_U123', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local1_U123', figure=figuraL1_U123, className='teste'),
            html.H2(children=[daq.Indicator(id='alarme_Local1_U123', label=x, value=True, size=40, color=alarmeL1_U123)],
                    style={"color": alarmeL1_U123, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local1_U123', interval=1 * 180000, n_intervals=0)
        ], className="six columns"),
    ], className='row'),

    html.Div([
        html.Div([
            html.H3('Local2_ACeT', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local2_ACeT', figure=figuraL2_ACeT, className="teste"),
            html.H2(children=[daq.Indicator(id='alarme_Local2_ACeT', label=x, value=True, size=40, color=teste1)],
                    style={"color": teste1, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local2_ACeT', interval=1 * 180000, n_intervals=0)
        ], className='six columns'),

        html.Div([
            html.H3('Local2_U123', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local2_U123', figure=figuraL2_U123, className='teste'),
            html.H2(children=[daq.Indicator(id='alarme_Local2_U123', label=x, value=True, size=40, color=alarmeL2_U123)],
                    style={"color": alarmeL2_U123, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local2_U123', interval=1 * 180000, n_intervals=0)
        ], className="six columns"),
    ], className='row'),

    html.Div([
        html.Div([
            html.H3('Local3_ACeT', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local3_ACeT', figure=figuraL3_ACeT, className="teste"),
            html.H2(children=[daq.Indicator(id='alarme_Local3_ACeT', label=x, value=True, size=40, color=teste1)],
                    style={"color": teste1, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local3_ACeT', interval=1 * 180000, n_intervals=0)
        ], className='six columns'),

        html.Div([
            html.H3('Local3_U123', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local3_U123', figure=figuraL3_U123, className='teste'),
            html.H2(children=[daq.Indicator(id='alarme_Local3_U123', label=x, value=True, size=40, color=alarmeL3_U123)],
                    style={"color": alarmeL3_U123, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local3_U123', interval=1 * 180000, n_intervals=0)
        ], className="six columns"),
    ], className='row'),

    html.Div([
        html.Div([
            html.H3('Local4_ACeT', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local4_ACeT', figure=figuraL4_ACeT, className="teste"),
            html.H2(children=[daq.Indicator(id='alarme_Local4_ACeT', label=x, value=True, size=40, color=teste1)],
                    style={"color": teste1, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local4_ACeT', interval=1 * 180000, n_intervals=0)
        ], className='six columns'),

        html.Div([
            html.H3('Local4_U123', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local4_U123', figure=figuraL4_U123, className='teste'),
            html.H2(children=[daq.Indicator(id='alarme_Local4_U123', label=x, value=True, size=40, color=alarmeL4_U123)],
                    style={"color": alarmeL4_U123, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local4_U123', interval=1 * 180000, n_intervals=0)
        ], className="six columns"),
    ], className='row'),

    html.Div([
        html.Div([
            html.H3('Local5_ACeT', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local5_ACeT', figure=figuraL5_ACeT, className="teste"),
            html.H2(children=[daq.Indicator(id='alarme_Local5_ACeT', label=x, value=True, size=40, color=teste1)],
                    style={"color": teste1, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local5_ACeT', interval=1 * 180000, n_intervals=0)
        ], className='six columns'),

        html.Div([
            html.H3('Local5_U123', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local5_U123', figure=figuraL5_U123, className='teste'),
            html.H2(children=[daq.Indicator(id='alarme_Local5_U123', label=x, value=True, size=40, color=alarmeL5_U123)],
                    style={"color": alarmeL5_U123, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local5_U123', interval=1 * 180000, n_intervals=0)
        ], className="six columns"),
    ], className='row'),

    html.Div([
        html.Div([
            html.H3('Local6_ACeT', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local6_ACeT', figure=figuraL6_ACeT, className="teste"),
            html.H2(children=[daq.Indicator(id='alarme_Local6_ACeT', label=x, value=True, size=40, color=teste1)],
                    style={"color": teste1, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local6_ACeT', interval=1 * 180000, n_intervals=0)
        ], className='six columns'),

        html.Div([
            html.H3('Local6_U123', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local6_U123', figure=figuraL6_U123, className='teste'),
            html.H2(children=[daq.Indicator(id='alarme_Local6_U123', label=x, value=True, size=40, color=alarmeL6_U123)],
                    style={"color": alarmeL6_U123, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local6_U123', interval=1 * 180000, n_intervals=0)
        ], className="six columns"),
    ], className='row'),

    html.Div([
        html.Div([
            html.H3('Local7_ACeT', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local7_ACeT', figure=figuraL7_ACeT, className="teste"),
            html.H2(children=[daq.Indicator(id='alarme_Local7_ACeT', label=x, value=True, size=40, color=teste1)],
                    style={"color": teste1, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local7_ACeT', interval=1 * 180000, n_intervals=0)
        ], className='six columns'),

        html.Div([
            html.H3('Local7_U123', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local7_U123', figure=figuraL7_U123, className='teste'),
            html.H2(children=[daq.Indicator(id='alarme_Local7_U123', label=x, value=True, size=40, color=alarmeL7_U123)],
                    style={"color": alarmeL7_U123, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local7_U123', interval=1 * 180000, n_intervals=0)
        ], className="six columns"),
    ], className='row'),

    html.Div([
        html.Div([
            html.H3('Local8_ACeT', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local8_ACeT', figure=figuraL8_ACeT, className="teste"),
            html.H2(children=[daq.Indicator(id='alarme_Local8_ACeT', label=x, value=True, size=40, color=teste1)],
                    style={"color": teste1, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local8_ACeT', interval=1 * 180000, n_intervals=0)
        ], className='six columns'),

        html.Div([
            html.H3('Local8_U123', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local8_U123', figure=figuraL8_U123, className='teste'),
            html.H2(children=[daq.Indicator(id='alarme_Local8_U123', label=x, value=True, size=40, color=alarmeL8_U123)],
                    style={"color": alarmeL8_U123, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local8_U123', interval=1 * 180000, n_intervals=0)
        ], className="six columns"),
    ], className='row'),

    html.Div([
        html.Div([
            html.H3('Local9_ACeT', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local9_ACeT', figure=figuraL9_ACeT, className="teste"),
            html.H2(children=[daq.Indicator(id='alarme_Local9_ACeT', label=x, value=True, size=40, color=teste1)],
                    style={"color": teste1, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local9_ACeT', interval=1 * 180000, n_intervals=0)
        ], className='six columns'),

        html.Div([
            html.H3('Local9_U123', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local9_U123', figure=figuraL9_U123, className='teste'),
            html.H2(children=[daq.Indicator(id='alarme_Local9_U123', label=x, value=True, size=40, color=alarmeL9_U123)],
                    style={"color": alarmeL9_U123, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local9_U123', interval=1 * 180000, n_intervals=0)
        ], className="six columns"),
    ], className='row'),

    html.Div([
        html.Div([
            html.H3('Local10_ACeT', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local10_ACeT', figure=figuraL10_ACeT, className="teste"),
            html.H2(children=[daq.Indicator(id='alarme_Local10_ACeT', label=x, value=True, size=40, color=teste1)],
                    style={"color": teste1, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local10_ACeT', interval=1 * 180000, n_intervals=0)
        ], className='six columns'),

        html.Div([
            html.H3('Local10_U123', style={"color": "#0039a6", "text-align": "center"}),
            dcc.Graph(id='Local10_U123', figure=figuraL10_U123, className='teste'),
            html.H2(children=[daq.Indicator(id='alarme_Local10_U123', label=x, value=True, size=40, color=alarmeL10_U123)],
                    style={"color": alarmeL10_U123, "text-align": "center"}),
            dcc.Interval(id='interval-component_Local10_U123', interval=1 * 180000, n_intervals=0)
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

#LOCAL 1____________________________________________________________________________________________________________________
# (17) ATUALIZAÇÃO DO GRÁFICO ACeT LOCAL1
@callback(Output('Local1_ACeT', 'figure'),
          Input('interval-component_Local1_ACeT', 'n_intervals'))
def update_xyz_temperatura5(n):
    df_Local_1 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL1_ACeT = of.graficos_df_ACeT(df_Local_1)
    return figuraL1_ACeT

# (18) ATUALIZAÇÃO do sinal de alarme de ACeT LOCAL1
@callback(Output('alarme_Local1_ACeT', 'color'),
          Input('interval-component_Local1_ACeT', 'n_intervals'))
def funcao_alarme9(n):
    df_Local_1 = of.importa_df("https://thingspeak.com/channels/1962136/")
    teste = "#9C1FBD"
    teste1 = "#f70d1a"
    teste2 = "#EEEE0A"
    teste3 = "#3DEC0A"
    return teste

# (19) ATUALIZAÇÃO DO do gráfico U123 LOCAL1
@callback(Output('Local1_U123', 'figure'),
          Input('interval-component_Local1_U123', 'n_intervals'))
def update_Umidades5(n):
    df_Local_1 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL1_U123 = of.graficos_df_U123(df_Local_1)
    return figuraL1_U123

# (20) ATUALIZAÇÃO DO sinal de alarme de U123 LOCAL1
@callback(Output('alarme_Local1_U123', 'color'),
          Input('interval-component_Local1_U123', 'n_intervals'))
def funcao_alarme10(n):
    df_Local_1 = of.importa_df("https://thingspeak.com/channels/1962136/")
    alarmeL1_U123 = of.alarme_U123(df_Local_1, 30, 10, -6, "Umidade3")
    return alarmeL1_U123

#LOCAL 2____________________________________________________________________________________________________________________
# (21) ATUALIZAÇÃO DO GRÁFICO ACeT LOCAL2
@callback(Output('Local2_ACeT', 'figure'),
          Input('interval-component_Local2_ACeT', 'n_intervals'))
def update_xyz_temperatura6(n):
    df_Local_2 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL2_ACeT = of.graficos_df_ACeT(df_Local_2)
    return figuraL2_ACeT

# (22) ATUALIZAÇÃO do sinal de alarme de ACeT LOCAL2
@callback(Output('alarme_Local2_ACeT', 'color'),
          Input('interval-component_Local2_ACeT', 'n_intervals'))
def funcao_alarme11(n):
    df_Local_2 = of.importa_df("https://thingspeak.com/channels/1962136/")
    teste = "#9C1FBD"
    teste1 = "#f70d1a"
    teste2 = "#EEEE0A"
    teste3 = "#3DEC0A"
    return teste

# (23) ATUALIZAÇÃO DO do gráfico U123 LOCAL2
@callback(Output('Local2_U123', 'figure'),
          Input('interval-component_Local2_U123', 'n_intervals'))
def update_Umidades6(n):
    df_Local_2 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL2_U123 = of.graficos_df_U123(df_Local_2)
    return figuraL2_U123

# (24) ATUALIZAÇÃO DO sinal de alarme de U123 LOCAL2
@callback(Output('alarme_Local2_U123', 'color'),
          Input('interval-component_Local2_U123', 'n_intervals'))
def funcao_alarme12(n):
    df_Local_2 = of.importa_df("https://thingspeak.com/channels/1962136/")
    alarmeL2_U123 = of.alarme_U123(df_Local_2, 30, 10, -6, "Umidade3")
    return alarmeL2_U123

#LOCAL 3____________________________________________________________________________________________________________________
# (25) ATUALIZAÇÃO DO GRÁFICO ACeT LOCAL3
@callback(Output('Local3_ACeT', 'figure'),
          Input('interval-component_Local3_ACeT', 'n_intervals'))
def update_xyz_temperatura7(n):
    df_Local_3 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL3_ACeT = of.graficos_df_ACeT(df_Local_3)
    return figuraL3_ACeT

# (26) ATUALIZAÇÃO do sinal de alarme de ACeT LOCAL3
@callback(Output('alarme_Local3_ACeT', 'color'),
          Input('interval-component_Local3_ACeT', 'n_intervals'))
def funcao_alarme13(n):
    df_Local_3 = of.importa_df("https://thingspeak.com/channels/1962136/")
    teste = "#9C1FBD"
    teste1 = "#f70d1a"
    teste2 = "#EEEE0A"
    teste3 = "#3DEC0A"
    return teste

# (27) ATUALIZAÇÃO DO do gráfico U123 LOCAL3
@callback(Output('Local3_U123', 'figure'),
          Input('interval-component_Local3_U123', 'n_intervals'))
def update_Umidades7(n):
    df_Local_3 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL3_U123 = of.graficos_df_U123(df_Local_3)
    return figuraL3_U123

# (28) ATUALIZAÇÃO DO sinal de alarme de U123 LOCAL3
@callback(Output('alarme_Local3_U123', 'color'),
          Input('interval-component_Local3_U123', 'n_intervals'))
def funcao_alarme14(n):
    df_Local_3 = of.importa_df("https://thingspeak.com/channels/1962136/")
    alarmeL3_U123 = of.alarme_U123(df_Local_3, 30, 10, -6, "Umidade3")
    return alarmeL3_U123

#LOCAL 4____________________________________________________________________________________________________________________
# (29) ATUALIZAÇÃO DO GRÁFICO ACeT LOCAL4
@callback(Output('Local4_ACeT', 'figure'),
          Input('interval-component_Local4_ACeT', 'n_intervals'))
def update_xyz_temperatura8(n):
    df_Local_4 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL4_ACeT = of.graficos_df_ACeT(df_Local_4)
    return figuraL4_ACeT

# (30) ATUALIZAÇÃO do sinal de alarme de ACeT LOCAL4
@callback(Output('alarme_Local4_ACeT', 'color'),
          Input('interval-component_Local4_ACeT', 'n_intervals'))
def funcao_alarme15(n):
    df_Local_4 = of.importa_df("https://thingspeak.com/channels/1962136/")
    teste = "#9C1FBD"
    teste1 = "#f70d1a"
    teste2 = "#EEEE0A"
    teste3 = "#3DEC0A"
    return teste

# (31) ATUALIZAÇÃO DO do gráfico U123 LOCAL4
@callback(Output('Local4_U123', 'figure'),
          Input('interval-component_Local4_U123', 'n_intervals'))
def update_Umidades8(n):
    df_Local_4 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL4_U123 = of.graficos_df_U123(df_Local_4)
    return figuraL4_U123

# (32) ATUALIZAÇÃO DO sinal de alarme de U123 LOCAL4
@callback(Output('alarme_Local4_U123', 'color'),
          Input('interval-component_Local4_U123', 'n_intervals'))
def funcao_alarme16(n):
    df_Local_4 = of.importa_df("https://thingspeak.com/channels/1962136/")
    alarmeL4_U123 = of.alarme_U123(df_Local_4, 30, 10, -6, "Umidade3")
    return alarmeL4_U123

#LOCAL 5____________________________________________________________________________________________________________________
# (33) ATUALIZAÇÃO DO GRÁFICO ACeT LOCAL5
@callback(Output('Local5_ACeT', 'figure'),
          Input('interval-component_Local5_ACeT', 'n_intervals'))
def update_xyz_temperatura9(n):
    df_Local_5 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL5_ACeT = of.graficos_df_ACeT(df_Local_5)
    return figuraL5_ACeT

# (34) ATUALIZAÇÃO do sinal de alarme de ACeT LOCAL5
@callback(Output('alarme_Local5_ACeT', 'color'),
          Input('interval-component_Local5_ACeT', 'n_intervals'))
def funcao_alarme17(n):
    df_Local_5 = of.importa_df("https://thingspeak.com/channels/1962136/")
    teste = "#9C1FBD"
    teste1 = "#f70d1a"
    teste2 = "#EEEE0A"
    teste3 = "#3DEC0A"
    return teste

# (35) ATUALIZAÇÃO DO do gráfico U123 LOCAL5
@callback(Output('Local5_U123', 'figure'),
          Input('interval-component_Local5_U123', 'n_intervals'))
def update_Umidades9(n):
    df_Local_5 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL5_U123 = of.graficos_df_U123(df_Local_5)
    return figuraL5_U123

# (36) ATUALIZAÇÃO DO sinal de alarme de U123 LOCAL5
@callback(Output('alarme_Local5_U123', 'color'),
          Input('interval-component_Local5_U123', 'n_intervals'))
def funcao_alarme18(n):
    df_Local_5 = of.importa_df("https://thingspeak.com/channels/1962136/")
    alarmeL5_U123 = of.alarme_U123(df_Local_5, 30, 10, -6, "Umidade3")
    return alarmeL5_U123

#LOCAL 6____________________________________________________________________________________________________________________
# (37) ATUALIZAÇÃO DO GRÁFICO ACeT LOCAL6
@callback(Output('Local6_ACeT', 'figure'),
          Input('interval-component_Local6_ACeT', 'n_intervals'))
def update_xyz_temperatura10(n):
    df_Local_6 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL6_ACeT = of.graficos_df_ACeT(df_Local_6)
    return figuraL6_ACeT

# (38) ATUALIZAÇÃO do sinal de alarme de ACeT LOCAL6
@callback(Output('alarme_Local6_ACeT', 'color'),
          Input('interval-component_Local6_ACeT', 'n_intervals'))
def funcao_alarme19(n):
    df_Local_6 = of.importa_df("https://thingspeak.com/channels/1962136/")
    teste = "#9C1FBD"
    teste1 = "#f70d1a"
    teste2 = "#EEEE0A"
    teste3 = "#3DEC0A"
    return teste

# (39) ATUALIZAÇÃO DO do gráfico U123 LOCAL6
@callback(Output('Local6_U123', 'figure'),
          Input('interval-component_Local6_U123', 'n_intervals'))
def update_Umidades10(n):
    df_Local_6 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL6_U123 = of.graficos_df_U123(df_Local_6)
    return figuraL6_U123

# (40) ATUALIZAÇÃO DO sinal de alarme de U123 LOCAL6
@callback(Output('alarme_Local6_U123', 'color'),
          Input('interval-component_Local6_U123', 'n_intervals'))
def funcao_alarme20(n):
    df_Local_6 = of.importa_df("https://thingspeak.com/channels/1962136/")
    alarmeL6_U123 = of.alarme_U123(df_Local_6, 30, 10, -6, "Umidade3")
    return alarmeL6_U123

#LOCAL 7____________________________________________________________________________________________________________________
# (41) ATUALIZAÇÃO DO GRÁFICO ACeT LOCAL7
@callback(Output('Local7_ACeT', 'figure'),
          Input('interval-component_Local7_ACeT', 'n_intervals'))
def update_xyz_temperatura11(n):
    df_Local_7 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL7_ACeT = of.graficos_df_ACeT(df_Local_7)
    return figuraL7_ACeT

# (42) ATUALIZAÇÃO do sinal de alarme de ACeT LOCAL7
@callback(Output('alarme_Local7_ACeT', 'color'),
          Input('interval-component_Local7_ACeT', 'n_intervals'))
def funcao_alarme21(n):
    df_Local_7 = of.importa_df("https://thingspeak.com/channels/1962136/")
    teste = "#9C1FBD"
    teste1 = "#f70d1a"
    teste2 = "#EEEE0A"
    teste3 = "#3DEC0A"
    return teste

# (43) ATUALIZAÇÃO DO do gráfico U123 LOCAL7
@callback(Output('Local7_U123', 'figure'),
          Input('interval-component_Local7_U123', 'n_intervals'))
def update_Umidades11(n):
    df_Local_7 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL7_U123 = of.graficos_df_U123(df_Local_7)
    return figuraL7_U123

# (44) ATUALIZAÇÃO DO sinal de alarme de U123 LOCAL7
@callback(Output('alarme_Local7_U123', 'color'),
          Input('interval-component_Local7_U123', 'n_intervals'))
def funcao_alarme22(n):
    df_Local_7 = of.importa_df("https://thingspeak.com/channels/1962136/")
    alarmeL7_U123 = of.alarme_U123(df_Local_7, 30, 10, -6, "Umidade3")
    return alarmeL7_U123

#LOCAL 8____________________________________________________________________________________________________________________
# (45) ATUALIZAÇÃO DO GRÁFICO ACeT LOCAL8
@callback(Output('Local8_ACeT', 'figure'),
          Input('interval-component_Local8_ACeT', 'n_intervals'))
def update_xyz_temperatura12(n):
    df_Local_8 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL8_ACeT = of.graficos_df_ACeT(df_Local_8)
    return figuraL8_ACeT

# (46) ATUALIZAÇÃO do sinal de alarme de ACeT LOCAL8
@callback(Output('alarme_Local8_ACeT', 'color'),
          Input('interval-component_Local8_ACeT', 'n_intervals'))
def funcao_alarme23(n):
    df_Local_8 = of.importa_df("https://thingspeak.com/channels/1962136/")
    teste = "#9C1FBD"
    teste1 = "#f70d1a"
    teste2 = "#EEEE0A"
    teste3 = "#3DEC0A"
    return teste

# (47) ATUALIZAÇÃO DO do gráfico U123 LOCAL8
@callback(Output('Local8_U123', 'figure'),
          Input('interval-component_Local8_U123', 'n_intervals'))
def update_Umidades12(n):
    df_Local_8 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL8_U123 = of.graficos_df_U123(df_Local_8)
    return figuraL8_U123

# (48) ATUALIZAÇÃO DO sinal de alarme de U123 LOCAL8
@callback(Output('alarme_Local8_U123', 'color'),
          Input('interval-component_Local8_U123', 'n_intervals'))
def funcao_alarme24(n):
    df_Local_8 = of.importa_df("https://thingspeak.com/channels/1962136/")
    alarmeL8_U123 = of.alarme_U123(df_Local_8, 30, 10, -6, "Umidade3")
    return alarmeL8_U123

#LOCAL 9____________________________________________________________________________________________________________________
# (49) ATUALIZAÇÃO DO GRÁFICO ACeT LOCAL9
@callback(Output('Local9_ACeT', 'figure'),
          Input('interval-component_Local9_ACeT', 'n_intervals'))
def update_xyz_temperatura13(n):
    df_Local_9 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL9_ACeT = of.graficos_df_ACeT(df_Local_9)
    return figuraL9_ACeT

# (50) ATUALIZAÇÃO do sinal de alarme de ACeT LOCAL9
@callback(Output('alarme_Local9_ACeT', 'color'),
          Input('interval-component_Local9_ACeT', 'n_intervals'))
def funcao_alarme25(n):
    df_Local_9 = of.importa_df("https://thingspeak.com/channels/1962136/")
    teste = "#9C1FBD"
    teste1 = "#f70d1a"
    teste2 = "#EEEE0A"
    teste3 = "#3DEC0A"
    return teste

# (51) ATUALIZAÇÃO DO do gráfico U123 LOCAL9
@callback(Output('Local9_U123', 'figure'),
          Input('interval-component_Local9_U123', 'n_intervals'))
def update_Umidades13(n):
    df_Local_9 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL9_U123 = of.graficos_df_U123(df_Local_9)
    return figuraL9_U123

# (52) ATUALIZAÇÃO DO sinal de alarme de U123 LOCAL9
@callback(Output('alarme_Local9_U123', 'color'),
          Input('interval-component_Local9_U123', 'n_intervals'))
def funcao_alarme26(n):
    df_Local_9 = of.importa_df("https://thingspeak.com/channels/1962136/")
    alarmeL9_U123 = of.alarme_U123(df_Local_9, 30, 10, -6, "Umidade3")
    return alarmeL9_U123

#LOCAL 10___________________________________________________________________________________________________________________
# (53) ATUALIZAÇÃO DO GRÁFICO ACeT LOCAL10
@callback(Output('Local10_ACeT', 'figure'),
          Input('interval-component_Local10_ACeT', 'n_intervals'))
def update_xyz_temperatura14(n):
    df_Local_10 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL10_ACeT = of.graficos_df_ACeT(df_Local_10)
    return figuraL10_ACeT

# (54) ATUALIZAÇÃO do sinal de alarme de ACeT LOCAL10
@callback(Output('alarme_Local10_ACeT', 'color'),
          Input('interval-component_Local10_ACeT', 'n_intervals'))
def funcao_alarme27(n):
    df_Local_10 = of.importa_df("https://thingspeak.com/channels/1962136/")
    teste = "#9C1FBD"
    teste1 = "#f70d1a"
    teste2 = "#EEEE0A"
    teste3 = "#3DEC0A"
    return teste

# (55) ATUALIZAÇÃO DO do gráfico U123 LOCAL10
@callback(Output('Local10_U123', 'figure'),
          Input('interval-component_Local10_U123', 'n_intervals'))
def update_Umidades14(n):
    df_Local_10 = of.importa_df("https://thingspeak.com/channels/1962136/")
    figuraL10_U123 = of.graficos_df_U123(df_Local_10)
    return figuraL10_U123

# (56) ATUALIZAÇÃO DO sinal de alarme de U123 LOCAL10
@callback(Output('alarme_Local10_U123', 'color'),
          Input('interval-component_Local10_U123', 'n_intervals'))
def funcao_alarme28(n):
    df_Local_10 = of.importa_df("https://thingspeak.com/channels/1962136/")
    alarmeL10_U123 = of.alarme_U123(df_Local_10, 30, 10, -6, "Umidade3")
    return alarmeL10_U123

#FIM________________________________________________________________________________________________________________________

#!
#layout.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
#!