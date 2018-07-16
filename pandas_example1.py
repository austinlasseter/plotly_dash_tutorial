
# imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# read in the dataset
url="https://raw.githubusercontent.com/austinlasseter/plotly_dash_tutorial/master/titanic.csv"
df=pd.read_csv(url)
# group survival results by sex and cabin class
sex_survive=df.groupby(['Sex', 'Pclass']).Survived.mean()
sex_survive=sex_survive*100
mylist=list(sex_survive)

# instantiate the class
app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
app.title = 'Titanic!'

# define the layout
app.layout = html.Div(children=[
    html.H1(children='Titanic!'),
    html.Div(children='Who survived the sinking of the Titanic?'),
    dcc.Graph(
        id='titanic-graph',
        figure={
            'data': [
                {'x': ['1st Class', '2nd Class', '3rd Class'], 'y': [mylist[0], mylist[1], mylist[2]], 'type': 'bar', 'name': 'Female'},
                {'x': ['1st Class', '2nd Class', '3rd Class'], 'y': [mylist[3], mylist[4], mylist[5]], 'type': 'bar', 'name': 'Male'},
            ],
            'layout': {
                'title': 'Survival Rate by Sex',
                'xaxis':{'title':'Cabin Class'},
                'yaxis':{'title':'Percentage Survival'},
            }
        }
    )
])

# execute
if __name__ == '__main__':
    app.run_server()
