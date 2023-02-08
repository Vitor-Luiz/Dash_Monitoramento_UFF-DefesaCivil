import dash
from dash import html
from dash import html
import dash

# https://bootswatch.com

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.H2(children='Monitoramento UFF'),
        html.Div(children='''Acompanhamento em tempo real (delay 3min) dos sensores de deslizamento, temperatura
        e umidades.''')])