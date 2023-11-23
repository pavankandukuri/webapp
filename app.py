from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the default URL
@app.route('/')
def home():
    # Render the 'index.html' template
    return "The two most important days in your life are the day you are born and the day you find out why.

Whenever you find yourself on the side of the majority, it is time to reform (or pause and reflect).

Courage is resistance to fear, mastery of fear—not absence of fear.

The secret of getting ahead is getting started.

Kindness is a language which the deaf can hear and the blind can see.

Don't let schooling interfere with your education.

If you tell the truth, you don't have to remember anything.

The more I learn about people, the more I like my dog.

The best way to cheer yourself up is to try to cheer somebody else up.

The man who does not read has no advantage over the man who cannot read."

# Run the application if the script is executed
if __name__ == '__main__':
    # Set debug=True to enable auto-reloading of the server on code changes
    app.run()
