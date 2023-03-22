# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Max" # write your name
    age = "9" # write your age

    return render_template('index.html', name = name, age = age)

# define the route to father webpage
@app.route("/father")
def father():

    name = "Tony"
    age = "45"

    return render_template('index.html', name = name, age = age)

# define the route to mother webpage
@app.route("/mother")
def mother():

    name = "Cerise"
    age = "43"

    return render_template('index.html', name = name, age = age)

# define the route to friends webpage
@app.route("/friend")
def friend():

    name = "Sid"
    age = "9"

    return render_template('index.html', name = name, age = age)

# add other routes, if you want

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
