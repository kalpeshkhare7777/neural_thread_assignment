from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/refresh')
def refresh():
    # Add any processing needed before refreshing the page
    return render_template('index.html')

@app.route('/run_model')
def run_model():
    # Execute the model.py script using subprocess
    subprocess.run(['python', 'model.py'])
    return ''

if __name__ == '__main__':
    app.run(debug=True)
