from dash import Dash, html, dcc
import dash

#AWS Elastic Beanstalk necessita que o aplicativo principal se chame application.py

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets)
application = app.server #AWS elastic beanstalk
app.title='Monitoramento UFF'

app.layout = html.Div([
	html.H1('Universidade Federal Fluminense/Defesa Civil'),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),

	dash.page_container
])

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
	application.run(debug=True, port=8080) #AWS elastic beanstalk