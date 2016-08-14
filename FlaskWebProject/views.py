"""Routes and views for the UOTD Flask application."""

from datetime import date, datetime
from flask import abort, render_template, url_for
from FlaskWebProject import app, azuretablestorage, settings

repository = azuretablestorage.Repository(settings.REPOSITORY_SETTINGS)


@app.route("/")
def home():
    """Render the home page which displays the UUID of the day."""
    uuid = repository.get_uotd()
    today = date.today().strftime("%A, %d %B %Y")
    return render_template("index.html", uuid=uuid, today=today)


@app.route("/archive", defaults={'partition_key': None})
@app.route("/archive/<partition_key>")
def archive(partition_key):
    """Render the archive page which displays all the UUIDs for a month.

    If no partition key is specified then the current month is used to form the
    key.
    """
    if partition_key is None:
        date_obj = date.today()
        partition_key = date_obj.strftime("%Y%m")
    else:
        try:
            date_obj = datetime.strptime(partition_key, "%Y%m")
        except ValueError:
            abort(404)

    uuids = repository.get_uuids(partition_key)
    display_month = date_obj.strftime("%B %Y")

    # Work out the next and previous months and their URLs
    if date_obj.month == 12:
        # Month is December so move to next year
        next_month = date(date_obj.year + 1, 1, date_obj.day)
    else:
        next_month = date(date_obj.year, date_obj.month + 1, date_obj.day)

    if date_obj.month == 1:
        # Month is January so move to previous year
        prev_month = date(date_obj.year - 1, 12, date_obj.day)
    else:
        prev_month = date(date_obj.year, date_obj.month - 1, date_obj.day)

    next_url = url_for('archive', partition_key=next_month.strftime("%Y%m"))
    prev_url = url_for('archive', partition_key=prev_month.strftime("%Y%m"))

    return render_template("archive.html",
                           uuids=uuids,
                           display_month=display_month,
                           next_url=next_url,
                           prev_url=prev_url)


@app.template_filter("display_day")
def display_day(uuid):
    """Display a readable form of the day for a given UUID entity."""
    date_str = "{0}{1}".format(uuid.PartitionKey, uuid.RowKey)
    date_obj = datetime.strptime(date_str, "%Y%m%d")
    return date_obj.strftime("%A, %d")
