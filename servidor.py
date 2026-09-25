from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv
from config_server import Config #Aquí importa las configuraciones y los archivos de config_sesrver

class Config:
    SECRET_KEY = os.getenv("API_KEY") #Acá las configura

app= Flask(__name__)
app.config.from_object(Config) #Aqui las aplica

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/admblog')
def admblog():
    return render_template('admblog.html')

if __name__=='__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
