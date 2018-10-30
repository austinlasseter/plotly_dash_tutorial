import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
app.title = 'Deloitte Dash'

app.layout = html.Div(children=[
    html.H1('Hello Dash'),

    html.Div(
        children='Dash: A web application framework for Python.',
        style={
            'textAlign': 'right'
        }
    ),

    dcc.Graph(
        id='this_is_an_id',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [8, 4, 3], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'This is my graph',
                'xaxis':{'title':'This is the x axis'},
                'yaxis':{'title':'This is the y axis'},
            }
        }
    )]
)

if __name__ == '__main__':
    app.run_server()
