
# imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# read in the dataset
source="../00 resources/titanic.csv"
df=pd.read_csv(source)

# Build the Figure using Plotly Graph Objects
data = [go.Bar(
    x=df['Pclass'],
    y=df['Fare']
)]
layout = go.Layout(
    title='How much did Titanic passengers pay?',
    xaxis = {'title': 'What deck class were they?'},
    yaxis = {'title': 'What was their average fare?'},
)
my_fig = go.Figure(data=data, layout=layout)


# instantiate
app = dash.Dash()

# layout
app.layout = dcc.Graph(id='scatterplot2', figure = my_fig)

# execute
if __name__ == '__main__':
    app.run_server()
