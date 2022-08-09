import requests
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", date = get_update_date("index"))

@app.route("/pgp")
def pgp():
    with app.open_resource("static/pgp.txt") as file:
        pgp_key = file.read().decode("utf-8")
    return render_template("default.html", title = "PGP Key", text = pgp_key, date = get_update_date("default"))

def get_update_date(name):
    data = requests.get(f"https://api.github.com/repos/slightlyskepticalpotat/chenanthony-new/commits?path=/src/templates/{name}.html&page=1&per_page=1")
    return data.json()[0]["commit"]["committer"]["date"][:10]

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
