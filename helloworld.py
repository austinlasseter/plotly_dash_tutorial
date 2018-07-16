import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div('Hello World!')

if __name__ == '__main__':
    app.run_server()
