import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Set up the chart
trace1 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[20, 14, 23],
    name='SF Zoo'
)
trace2 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[12, 18, 29],
    name='LA Zoo'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='group'
)

zoo_fig = go.Figure(data=data, layout=layout)

########### Display it in Dash


app = dash.Dash()

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
app.title = 'Deloitte Dash'

app.layout = html.Div(children=[
    html.H1('My favorite zoo animals'),
    dcc.Graph(
        id='zoo_animals',
        figure=zoo_fig
    )]
)

if __name__ == '__main__':
    app.run_server()

# https://plot.ly/python/bar-charts/
