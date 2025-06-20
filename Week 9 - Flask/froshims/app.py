from cs50 import SQL
from flask import Flask, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///froshims.db")  # Database connection

SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbsee",
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name.")                   # Logica de validacao de dados inseridos pelo usuario

    sport = request.form.get("sport")
    if not sport:                                                                       # Logica de validacao de dados inseridos pelo usuario
        return render_template("error.html", message="Missing sport.")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport.")                  # Logica de validacao do dado sport inserido pelo usuario esta entre os esportes disponiveis

    db.execute("INSERT INTO registrants (name, sport) VALUES (?, ?)", name, sport)      # Insercao dos dados do usuario no banco de dados

    return render_template("success.html")


@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT name, sport FROM registrants")
    return render_template("registrants.html", registrants=registrants)
