from flask import Flask
from burclar import burclar
from flask_ngrok import run_with_ngrok
app = Flask(__name__)
run_with_ngrok(app)
@app.route("/")
def hello():
    return '<h1 style="color:green">Sitenin sonuna bir burç girmeniz gerekiyor.</h1>'
    
@app.route("/oglak")
def oglak():
    return burclar.oglak('gunluk')

@app.route("/koc")
def koc():
    return burclar.koc('gunluk')

@app.route("/boga")
def boga():
    return burclar.boga('gunluk') 

@app.route("/ikizler")
def ikizler():
    return burclar.ikizler('gunluk')


@app.route("/yengec")
def yengec():
    return burclar.yengec('gunluk')

@app.route("/aslan")
def aslan():
    return burclar.aslan('gunluk')

@app.route("/basak")
def basak():
    return burclar.basak('gunluk')

@app.route("/terazi")
def terazi():
    return burclar.terazi('gunluk')


@app.route("/akrep")
def akrep():
    return burclar.akrep('gunluk')

@app.route("/yay")
def yay():
    return burclar.yay('gunluk')

@app.route("/kova")
def kova():
    return burclar.kova('gunluk')

@app.route("/balik")
def balik():
    return burclar.balik('gunluk')


if __name__ == '__main__':
    app.run()
