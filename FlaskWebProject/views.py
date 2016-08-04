from datetime import date
from flask import render_template
from FlaskWebProject import app, azuretablestorage, settings

repository = azuretablestorage.Repository(settings.REPOSITORY_SETTINGS)


@app.route("/")
def home():
    uuid = repository.get_uotd()
    today = date.today().strftime("%A, %d %B %Y")
    return render_template("index.html", uuid=uuid, today=today)


@app.route("/archive")
def archive():
    return render_template("archive.html")
