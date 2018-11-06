# pip install dash-table==3.1.2
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

# read in the dataset
source="../00 resources/titanic.csv"
df=pd.read_csv(source)
df=df.loc[df['Age']>30] # Let's subset the age

# instantiate
app = dash.Dash(__name__)

# layout
app.layout = html.Div([
                html.H1('Titanic Dataset'),
                dash_table.DataTable(
                    id='table',
                    columns=[{"name": i, "id": i} for i in df.columns],
                    data=df.to_dict("rows"),
                )
            ])

# execute
if __name__ == '__main__':
    app.run_server(debug=True)

# https://dash.plot.ly/datatable
