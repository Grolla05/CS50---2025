import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session

# Configure application
app = Flask(__name__)
# É necessário configurar uma SECRET_KEY para usar o flash
app.config["SECRET_KEY"] = "sua_chave_secreta_aqui"

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        name = request.form.get("name")
        month_str = request.form.get("month")
        day_str = request.form.get("day")

        # Validação Refinada com Feedback
        if not name:
            flash("Name is required!", "error")
            return redirect("/")

        try:
            month = int(month_str)
            day = int(day_str)
        except (ValueError, TypeError):
            flash("Month and Day must be numbers!", "error")
            return redirect("/")

        if not (1 <= month <= 12):
            flash("Month must be between 1 and 12.", "error")
            return redirect("/")

        # Validação um pouco mais robusta para dias
        if not (1 <= day <= 31):
            flash("Day must be between 1 and 31.", "error")
            return redirect("/")

        # Inserir no banco de dados
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

        flash("Birthday added!", "success") # Mensagem de sucesso!
        return redirect("/")

    else: # GET
        birthdays = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays=birthdays)
