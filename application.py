from Flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    return "Hola fuckin mundo <3"