# This file has nothing to do with the actual website on GitHub Pages
# It is just used to test the website locally on localhost://

from flask import Flask, render_template
app = Flask(__name__, static_folder='', template_folder='')

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/tickets')
def tickets():
    return render_template('tickets.html')

app.run(host='0.0.0.0')