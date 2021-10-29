# /////////////////////////////////////////////////////////////////////
# Subj: Coding Dojo > Python > Flask > Fundamentals: form test
# By: Virgilio D. Cabading Jr.  Created: October 28, 2021
# /////////////////////////////////////////////////////////////////////

from flask import Flask, render_template, request, redirect    # Import Flask to allow us to create our app
app = Flask(__name__)                                           # Create a new instance of the Flask class called "app"

# **** Default App Route **********************************************
@app.route('/')                                         # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')

from flask import Flask, render_template, request, redirect # added request
            
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/')



# **** Handle invalid routes ******************************************
@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.