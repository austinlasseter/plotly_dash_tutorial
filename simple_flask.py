''' SIMPLE FLASK APP '''


''' import the Class '''
from flask import Flask     # flask is the framework here, while Flask is a Python class datatype.


''' instantiate the Class'''
app = Flask(__name__)       # once we import Flask, we need to create an instance of the Flask class for our web app.
                            # __name__ is a special variable that gets as value the string "__main__" when you’re executing the script.
                            # using "app" is an arbitrary convention, but be consistent.


''' define a function '''
@app.route('/my_app')       # This line is a function decorator, mapping the function follows to localhost:5000/my_app
def home():                 # we define a function that returns the string “Hey there!”.
    return "Hey there!"


''' execute '''
if __name__ == '__main__':  # This is only true when the script is executed. If it is imported, it will be false.
    app.run(debug=True)     # Prints out possible Python errors on the web page helping us trace the errors. Only use in Dev, not Prod.

# Source: https://pythonhow.com/how-a-flask-app-works/
