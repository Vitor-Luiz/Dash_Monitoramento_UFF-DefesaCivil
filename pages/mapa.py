from dash import html, dcc, callback, Input, Output
from dash.dependencies import Input, Output
import dash
import oficial_func as of

#DataFrame para o mapa
df_mapa = {"latitude":[-22.903936,-22.903937,-22.935979,-22.935980,-22.936045,-22.936046,-22.937911,-22.937912,
                       -22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979,
                       -22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979,-22.898979],
           "longitude":[-43.133884,-43.133885,-43.109102,-43.109103,-43.109104,-43.109105,-43.107782,-43.107783,
                        -43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131,
                        -43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131,-43.039131],
           "Sinais de Alerta":["UFF ACeT", "UFF U123", "Jurujuba1 ACeT", "Jurujuba1 U123",
                               "Jurujuba2 ACeT", "Jurujuba2 U123", "Jurujuba3 ACeT", "Jurujuba3 U123",
                               "Local1 ACeT", "Local1 U123", "Local2 ACeT", "Local2 U123", "Local3 ACeT", "Local3 U123",
                               "Local4 ACeT", "Local4 U123", "Local5 ACeT", "Local5 U123", "Local6 ACeT", "Local6 U123",
                               "Local7 ACeT", "Local7 U123", "Local8 ACeT", "Local8 U123", "Local9 ACeT", "Local9 U123",
                               "Local10 ACeT", "Local10 U123"]}

#Mapa de Monitoramento dos Alarmes
figura_mapa = of.grafico_df_mapa(df_mapa)


dash.register_page(__name__)
layout = html.Div([
    html.Div([
        html.H1('Mapa de Monitoramento', style={"color": "#0039a6", "text-align": "center"}),
        dcc.Graph(id='mapa', figure=figura_mapa, className="teste", style={'width': '100vw', 'height': '90vh'}),
        dcc.Interval(id='interval-component_mapa', interval=1 * 180000, n_intervals=0)
    ])
])

#ATUALIZAÇÃO DOS SINAIS DE ALERTA DOS MAPAS
@callback(Output('mapa', 'figure'),
          Input('interval-component_mapa', 'n_intervals'))
def update_mapa(n):
    figura_mapa = of.grafico_df_mapa(df_mapa)
    return figura_mapa