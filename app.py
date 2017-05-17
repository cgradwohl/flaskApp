# main Flask app file
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # returns a route to another file, by default looks into templates folder
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
