from app import app
from flask import render_template

@app.route("/")
@app.route("/index")

def index():
    noticia = "owesome. You may be able to book a flying taxi within three years"
    fonte= {"Jornal" : "BBC News", "Edicao":"18/10/2021" }
    return render_template('index.html', noticia=noticia,fonte=fonte)

@app.route('/contato')
def contato():
    return render_template('contato.html')