'''
A very simple dash app
'''

''' imports '''
import dash                             # dash is the framework, Dash is the class
import dash_html_components as html     # there are other dash libraries but this is the most basic

''' instantiate '''
app = dash.Dash()                       # Dash uses Flask as the web framework. The underlying Flask app is available at app.server

''' layout and functions '''
app.layout = html.Div('Goodbye Cruel World!')   # All dash apps will begin with 'app.layout = '. Note the 'html' call.

''' execute '''
if __name__ == '__main__':              # this ensures that the app is run only on execution, not on import
    app.run_server()
