from flask import Flask, request, render_template
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/o-nama')
def about():
    return render_template('about-us.html')

@app.route('/kontakt')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)