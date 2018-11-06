import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import base64


# Designate the image
deloitte = base64.b64encode(open('../00 resources/Deloitte_logo.png', 'rb').read())

########### Set up the chart
# Example taken from: https://plot.ly/~rmfoster/88#code
x = np.random.randn(500)
data = [go.Histogram(x=x)]
layout = go.Layout(
    title='This is a histogram about an IT survey',
    xaxis={'title':'How do you rate your satisfaction with Help Desk support?'},
    yaxis={'title':'Survey Respondents'}
)
fig = go.Figure(data=data, layout=layout)


########### Instantiate Dash

app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
app.title = 'Deloitte Dash'

########### APP LAYOUT ############
app.layout = html.Div([
    # Header and logo
                html.Div([
                    html.Img(
                        src='data:image/png;base64,{}'.format(deloitte.decode()),
                        style={'height':'30px', 'padding-top': '10px', 'padding-left': '12px'}
                        )
                ], style={'height':'45px', 'backgroundColor': 'rgb(0,0,0)'}, className='twelve columns'),
    # Title
                html.H4('Satisfaction survey', style={'text-align':'left'}),
    # Body
                html.Div([
                    dcc.Graph(
                    id='fig1',
                    figure=fig,
                    style={'height': '400px', 'align':'center'})
                ], className='twelve columns'),
    # Footer
                dcc.Markdown('Code source: [Plotly Website](https://plot.ly/python/histograms/)', className='twelve columns'),
                html.Div([
                    html.Div('copyright © 2018',
                        style={'color': 'rgb(255, 255, 255)',
                            'fontSize': 12,
                            'fontFamily':'Open Sans',
                            'font-weight': 'italic',
                            'text-align':'right',
                            'vertical-align': 'bottom',
                            'padding-right':'10px'
                        },
                        className='twelve columns')
                    ], style={'height':'30px', 'backgroundColor': 'rgb(0,0,0)'}, className='twelve columns')
            ])

####### Execute
if __name__ == '__main__':
    app.run_server()

# https://plot.ly/python/reference/
