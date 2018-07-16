
# imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

#
url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
c=pd.read_csv(url)

# output = len(df)

# instantiate
app = dash.Dash()

# layout
app.layout = html.Div(len(c))

# execute
if __name__ == '__main__':
    app.run_server()
