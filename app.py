from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the default URL
@app.route('/')
def home():
    # Render the 'index.html' template
    return "The two most important days in your life are the day you are born and the day you find out why."

# Run the application if the script is executed
if __name__ == '__main__':
    # Set debug=True to enable auto-reloading of the server on code changes
    app.run()
