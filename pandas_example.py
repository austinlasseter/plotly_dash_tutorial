
# imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# read in the dataset
url="https://raw.githubusercontent.com/austinlasseter/plotly_dash_tutorial/master/titanic.csv"
df=pd.read_csv(url)

# Build the Figure using Plotly Graph Objects
data = [go.Bar(
    x=df['Pclass'],
    y=df['Fare']
)]
layout = go.Layout(
    title='Who survived the Titanic?',
    xaxis = {'title': 'Category'},
    yaxis = {'title': 'Percent that survived'},
)
my_fig = go.Figure(data=data, layout=layout)


# instantiate
app = dash.Dash()

# layout
app.layout = dcc.Graph(id='scatterplot2', figure = my_fig)

# execute
if __name__ == '__main__':
    app.run_server()
