import random
import requests
import datetime
from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", time=datetime.datetime.now())


@app.route("/pgp")
def pgp():
    with app.open_resource("static/pgp.txt") as file:
        pgp_key = file.read().decode("utf-8")
    return render_template("default.html", title="PGP Key", text=pgp_key, time=datetime.datetime.now())


@app.route("/resume")
def resume():
    return render_template("resume.html", time=datetime.datetime.now())


@app.route("/projects")
def projects():
    featured_projects = [{"name": "chenanthony-new", "info": "Responsive portfolio website built with industry-standard frameworks. Previously PHP-based, now runs on Flask. Hosted on a GCP instance.", "url": "https://github.com/slightlyskepticalpotat/chenanthony-new", "img": url_for("static", filename="img/website.webp"), "tags": ['CSS', 'Flask', 'HTML', 'JS']}, {"name": "dogecoin-unofficial", "info": "Linux Snap for Dogecoin Core (the official Dogecoin wallet), available on the Snap Store. Packages official binaries for easy installation.", "url": "https://github.com/slightlyskepticalpotat/dogecoin-unofficial", "img": url_for("static", filename="img/dogecoin.webp"), "tags": ["Bash", "Linux", "Snap"]}, {"name": "mersenne-twister-tools:", "info": "A collection of scripts that implement and attack the famous Mersenne Twister PRNG (included in many standard libraries) and several variants.", "url": "https://github.com/slightlyskepticalpotat/mersenne-twister-tools", "img": url_for("static", filename="img/mt.webp"), "tags": ["Boost", "C++", "Cryptography", "Python"]}, {"name": "simple-markov:", "info": "Performant natural language generator using Markov chains. Can also be used to generate sequences of letters. Includes a Flask-based web frontend.", "url": "https://github.com/slightlyskepticalpotat/simple-markov", "img": url_for("static", filename="img/markov.webp"), "tags": ["AI", "C++", "Flask", "Python"]}, {"name": "snakewhisper:", "info": "Proof-of-concept of a simple end-to-end encrypted chat program. Currently supports two-way communication with elliptic curve key exchange.", "url": "https://github.com/slightlyskepticalpotat/snakewhisper", "img": url_for("static", filename="img/snake.webp"), "tags": ["Cryptography", "Networking", "Python"]}, {"name": "superlumic:", "info": "Secure command-line password manager written in C++. Allows users to create, save, and load encrypted (AES-256) password lists locally.", "url": "https://github.com/slightlyskepticalpotat/superlumic", "img": url_for("static", filename="img/super.webp"), "tags": ["AES", "C++", "Cryptography", "Make"]}]
    random.shuffle(featured_projects)
    all_projects = [{"name": "exactum", "info": "Flexible web monitoring tool for websites with no built-in notification system. Configured with YAML and supports desktop/email notifications and file logging.", "url": "https://github.com/slightlyskepticalpotat/exactum", "img": url_for("static", filename="img/exactum.webp"), "tags": ["Hackathon", "Networking", "Python", "SMTP"]}, {"name": "divoc", "info": "COVID-19 tracker that uses public APIs to calculate how many cases are within a certain distance of any address in Ontario. Includes self-assessment tool.", "url": "https://github.com/slightlyskepticalpotat/divoc", "img": url_for("static", filename="img/divoc.webp"), "tags": ["C++", "Hackathon", "Javascript", "PHP"]}, {"name": "submission-downloader", "info": "Tool for archiving code submissions to a wide variety of competitive programming sites in bulk. Available on PyPi. Useful for creating solution archives.", "url": "https://github.com/slightlyskepticalpotat/submission-downloader", "img": url_for("static", filename="img/subdl.webp"), "tags": ["Competitive Programming", "Python"]}, {"name": "ai-tictactoe", "info": "AI-powered tic-tac-toe game with a graphical user interface. Uses the minimax algorithm and alpha-beta pruning. Can be modified to play other games as well.", "url": "https://github.com/slightlyskepticalpotat/ai-tictactoe", "img": url_for("static", filename="img/aittt.webp"), "tags": ["AI", "CS50", "Python"]}, {"name": "cs50x-2021", "info": "Coursework for the 2021 CS50x: Introduction to Computer Science course offered by Harvard University. Wide variety of languages and technologies.", "url": "https://github.com/slightlyskepticalpotat/cs50x-2021", "img": url_for("static", filename="img/cs50x.webp"), "tags": ["C++", "CS50", "Javascript", "Python"]}, {"name": "cs50ai-2021", "info": "Coursework for the 2021 CS50ai: Introduction to Artificial Intelligence with Python course offered by Harvard University. Wide variety of algorithms.", "url": "https://github.com/slightlyskepticalpotat/cs50ai-2021", "img": url_for("static", filename="img/cs50ai.webp"), "tags": ["AI", "CS50", "Python"]}, {"name": "zoetrope-game-of-life", "info": "High-speed Python implementation of the famous cellular automaton. Turing-complete, it can theoretically simulate any computer algorithm in existence.", "url": "https://github.com/slightlyskepticalpotat/zoetrope-game-of-life", "img": url_for("static", filename="img/conway.webp"), "tags": ["AI", "Automaton", "Python"]}, {"name": "stonktrack", "info": "Financial tracker that can track stocks, cryptocurrencies, currencies, and other assets with simple configuration and a terminal-based GUI.", "url": "https://github.com/slightlyskepticalpotat/stonktrack", "img": url_for("static", filename="img/stonks.webp"), "tags": ["Cryptocurrency", "Finance", "Python"]}, {"name": "rc4-variants", "info": "Object-oriented implemention of RC4-drop[n], a modification of the simple and speedy RC4 stream cipher that defends against several attacks.", "url": "https://github.com/slightlyskepticalpotat/rc4-variants", "img": url_for("static", filename="img/arc4.webp"), "tags": ["Cryptography", "Python", "RC4"]}, {"name": "programming-solutions", "info": "Archive to hold all of my competitive programming solutions. Contains solutions and some explanations for CCC, Codeforces, DMOJ, CSES, and other sites.", "url": "https://github.com/slightlyskepticalpotat/programming-solutions", "img": url_for("static", filename="img/cp.webp"), "tags": ["C++", "Competitive Programming", "Java", "Python"]}, {"name": "cryptopals-solutions", "info": "Repository of my solutions to the cryptopals cryptography challenges. Incomplete, but I occasionally work on them for a while. Also contains several useful scripts.", "url": "https://github.com/slightlyskepticalpotat/cryptopals-solutions", "img": url_for("static", filename="img/aesecb.webp"), "tags": ["Cryptography", "Networking", "Python"]}, {"name": "bookmarkarchiver", "info": "Script to archive all of a browser's (Chromium-based or Firefox) bookmarks to the Internet Archive. Does not require registration, up to 100k pages/day.", "url": "https://github.com/slightlyskepticalpotat/bookmarkarchiver", "img": url_for("static", filename="img/bmar.webp"), "tags": ["Bookmarks", "Internet Archive", "Python"]}, {"name": "vorldle", "info": "Multi-platform Worldle clone implemented with Java's standard library GUI methods. Integrates country database and calculations for distance and bearing.", "url": "https://github.com/slightlyskepticalpotat/vorldle", "img": url_for("static", filename="img/vorldle.webp"), "tags": ["Database", "Java", "School"]}, {"name": "ctfoj", "info": "Open-source platform for hosting cybersecurity challenges and contests. Comprehensive test suite included. Used in production by the MGCI CTF Club.", "url": "https://github.com/jdabtieu/CTFOJ", "img": url_for("static", filename="img/ctfoj.webp"), "tags": ["CTF", "Flask", "Pytest", "Python"]}, {"name": "gennet", "info": "Innovative social media platform for families. Allows user to create \"trees\" for their family and populate the \"leaves\" with knowledge, anecdotes, or media.", "url": "https://github.com/AbdulBaseetShabi/GenNet", "img": url_for("static", filename="img/gennet.webp"), "tags": ["CSS", "HTML", "Javascript", "Python"]}, {"name": "shad-tile", "info": "Created for the SHAD program, this 15x15cm tile that showcases my interests and passions also doubles as a solderable breadboard. Created with KiCad.", "url": "https://drive.google.com/drive/folders/1npTcp0RNNdb8etQtxm8TY5L2R35EkcST?usp=sharing", "img": url_for("static", filename="img/shadtile.webp"), "tags": ["Hardware", "KiCad"]}, {"name": "mgcirobotics.com", "info": "Website for my robotics team, Audeamus 8574. Uses Jekyll to generate site from markdown files. Also integrates with MailChimp to send monthly newsletters.", "url": "https://mgcirobotics.com", "img": url_for("static", filename="img/robot.webp"), "tags": ["CSS", "HTML", "Jekyll", "JS"]}]
    random.shuffle(all_projects)
    return render_template("projects.html", featured=featured_projects, all=all_projects, time=datetime.datetime.now())


@app.route("/links")
def links():
    stored_links = [{"name": "Devpost", "url": "https://devpost.com/slightlyskepticalpotat"}, {"name": "DMOJ", "url": "https://dmoj.ca/user/slightlyskepticalpotat"}, {"name": "MGCI Robotics", "url": "https://mgcirobotics.com/"}, {"name": "The Reckoner", "url": "https://www.thereckoner.ca/author/anthonychen/"}, {"name": "Website Code", "url": "https://github.com/slightlyskepticalpotat/chenanthony-new"}, {"name": "MGCI Math", "url": "https://mgcimath.ca"}, {"name": "PyPi", "url": "https://pypi.org/search/?q=slightlyskepticalpotat"}, {"name": "MGCI CTF Club", "url": "https://ctfmgci.pythonanywhere.com/"}, {"name": "Audeamus 8574", "url": "https://www.thebluealliance.com/team/8574/"}, {"name": "Dogecoin Snap", "url": "https://snapcraft.io/dogecoin-unofficial"}, {"name": "Waterloo SE Webring", "url": "https://se-webring.xyz/"}, {"name": "Replit", "url": "https://replit.com/@slightlyskepticalpotat"}]
    stored_links.sort(key=lambda x: x["name"])
    return render_template("links.html", links=stored_links, time=datetime.datetime.now())


@app.route("/share/<path:path>")
def share(path):
    return send_from_directory("share", path)


@app.route("/writing")
def writing():
    return render_template("writing.html", time=datetime.datetime.now())


def get_update_date(name):
    # gets ratelimited too quickly
    data = requests.get(f"https://api.github.com/repos/slightlyskepticalpotat/chenanthony-new/commits?path=/src/templates/{name}.html&page=1&per_page=1")
    return data.json()[0]["commit"]["committer"]["date"][:10]


if __name__ == "__main__":
    app.run(host="0.0.0.0")
