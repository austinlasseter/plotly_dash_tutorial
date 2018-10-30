
# imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# read in the dataset
url="https://raw.githubusercontent.com/austinlasseter/plotly_dash_tutorial/master/titanic.csv"
df=pd.read_csv(url)

# define a function to display table
def generate_table(dataframe):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +
        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(len(dataframe))]
    )

# instantiate
app = dash.Dash()

# layout
app.layout = html.Div(generate_table(df))

# execute
if __name__ == '__main__':
    app.run_server()
