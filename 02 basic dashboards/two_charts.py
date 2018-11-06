
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import numpy as np

################ Generate the line plot ###########

data = [go.Scatter(
    x = ['Jan','Feb','Mar','Apr','May'],
    y = [3,2,5,4,7],
    mode = 'lines'
)]
layout = go.Layout(
    title = 'How often do I get new ideas?',
    xaxis={'title':'Months'},
    yaxis={'title':'New Ideas'}
)
line_plot = go.Figure(data=data,layout=layout)

############## Generate the scatter plot ###########

# generate random data
np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,31,30)

# define the data
data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)]
# define the layout
layout = go.Layout(
    title='Does anybody care about my ideas?',
    xaxis={'title':'Minutes I spent talking'},
    yaxis={'title':'People who listened to me'}
)
# combine data and layout into a dictionary
scatter_plot = dict(data=data, layout=layout )

######### Dash App ###########
app = dash.Dash()
app.title = '2-box dash app'
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'}) # CSS style sheet

app.layout = html.Div([
                dcc.Graph(
                    id='scatter',
                    figure=line_plot,
                    className='six columns'),
                dcc.Graph(
                    id='line',
                    figure=scatter_plot,
                    className='six columns')
            ])

if __name__ == '__main__':
    app.run_server(debug=True)
