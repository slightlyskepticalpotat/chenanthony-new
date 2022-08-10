import random
import requests
from flask import Flask, render_template, redirect, url_for

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
    featured_projects = [{"name": "chenanthony-new", "info": "Responsive portfolio website built with industry-standard frameworks. Previously PHP-based, now runs on Flask. Hosted on a GCP instance.", "url": "https://github.com/slightlyskepticalpotat/chenanthony-new", "img": url_for("static", filename="img/website.webp"), "tags": ["HTML", "CSS", "JS", "Flask"]}, {"name": "dogecoin-unofficial", "info": "Linux Snap for Dogecoin Core (the official Dogecoin wallet), available on the Snap Store. Packages official binaries for easy installation.", "url": "https://github.com/slightlyskepticalpotat/dogecoin-unofficial", "img": url_for("static", filename="img/dogecoin.webp"), "tags": ["Bash", "Linux", "Snap"]}, {"name": "mersenne-twister-tools:", "info": "A collection of scripts that implement and attack the famous Mersenne Twister PRNG (included in many standard libraries) and several variants.", "url": "https://github.com/slightlyskepticalpotat/mersenne-twister-tools", "img": url_for("static", filename="img/mt.webp"), "tags": ["Boost", "C++", "Python"]}, {"name": "simple-markov:", "info": "Performant natural language generator using Markov chains. Can also be used to generate sequences of letters. Includes a Flask-based web frontend.", "url": "https://github.com/slightlyskepticalpotat/simple-markov", "img": url_for("static", filename="img/markov.webp"), "tags": ["AI", "C++", "Flask", "Python"]}, {"name": "snakewhisper:", "info": "Proof-of-concept of a simple end-to-end encrypted chat program. Currently supports two-way communication with elliptic curve key exchange.", "url": "https://github.com/slightlyskepticalpotat/snakewhisper", "img": url_for("static", filename="img/snake.webp"), "tags": ["Cryptography", "Python", "Networking"]}, {"name": "superlumic:", "info": "Secure command-line password manager written in C++. Allows users to create, save, and load encrypted (AES-256) password lists locally.", "url": "https://github.com/slightlyskepticalpotat/superlumic", "img": url_for("static", filename="img/super.webp"), "tags": ["AES", "C++", "Cryptography", "Make"]}]
    random.shuffle(featured_projects)
    return render_template("projects.html", featured = featured_projects)

@app.route("/gallery")
def gallery():
    # radically different entire-page (except header and footer) gallery of images
    return "Under Construction"

@app.route("/links")
def links():
    stored_links = [{"name": "Devpost", "url": "https://devpost.com/slightlyskepticalpotat"}, {"name": "DMOJ", "url": "https://dmoj.ca/user/slightlyskepticalpotat"}, {"name": "MGCI Robotics", "url": "https://mgcirobotics.com/"}, {"name": "The Reckoner", "url": "https://www.thereckoner.ca/author/anthonychen/"}, {"name": "Website Code", "url": "https://github.com/slightlyskepticalpotat/chenanthony-new"}, {"name": "MGCI Math", "url": "https://mgcimath.ca"}, {"name": "PyPi", "url": "https://pypi.org/search/?q=slightlyskepticalpotat"}, {"name": "MGCI CTF Club", "url": "https://ctfmgci.pythonanywhere.com/"}, {"name": "Audeamus 8574", "url": "https://www.thebluealliance.com/team/8574/"}]
    stored_links.sort(key = lambda x: x["name"])
    return render_template("links.html", links = stored_links)

def get_update_date(name):
    # gets ratelimited too quickly
    data = requests.get(f"https://api.github.com/repos/slightlyskepticalpotat/chenanthony-new/commits?path=/src/templates/{name}.html&page=1&per_page=1")
    return data.json()[0]["commit"]["committer"]["date"][:10]

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
