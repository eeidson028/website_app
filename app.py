from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/marketing')
def marketing():
    return render_template('marketing.html')

@app.route('/database')
def database():
    return render_template('database.html')

@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == '__main__':
   app.run(debug = True)
