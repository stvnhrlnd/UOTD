from datetime import date
from flask import render_template
from FlaskWebProject import app, azuretablestorage, settings

repository = azuretablestorage.Repository(settings.REPOSITORY_SETTINGS)


@app.route("/")
@app.route("/home")
def home():
    uuid = repository.get_uotd()
    today = date.today().strftime("%A, %d %B %Y")
    return render_template("index.html", uuid=uuid, today=today)
