from flask import Flask, render_template

app= Flask(__name__)

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

if "__main__" == "__name__":
    app.run(host="0.0.0.0", port=8080, debug=True)
