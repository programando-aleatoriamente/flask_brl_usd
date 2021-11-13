from flask import Flask, render_template
from rules import brlusd

app = Flask(__name__)

@app.route('/real_dolar')
def index():
	
	return render_template('realdolar.html', name=brlusd.NAME, cota=brlusd.COTA, data=brlusd.DATA, high= brlusd.MAXIMUN, low= brlusd.MINIMUN)