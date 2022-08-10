import requests
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pgp")
def pgp():
    with app.open_resource("static/pgp.txt") as file:
        pgp_key = file.read().decode("utf-8")
    return render_template("default.html", title = "PGP Key", text = pgp_key)

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/projects")
def projects():
    # featured section with old blog-like cards, then the rest of the projects in random order with old project cards
    return "Under Construction"

@app.route("/gallery")
def gallery():
    # radically different entire-page (except header and footer) gallery of images
    return "Under Construction"

@app.route("/links")
def links():
    pass

def get_update_date(name):
    # gets ratelimited too quickly
    data = requests.get(f"https://api.github.com/repos/slightlyskepticalpotat/chenanthony-new/commits?path=/src/templates/{name}.html&page=1&per_page=1")
    return data.json()[0]["commit"]["committer"]["date"][:10]

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
