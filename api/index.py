from flask import Flask

app = Flask(__name__)


@app.route("/spaceapi.json")
def home():
    return {
        "api_compatibility": ["14"],
        "space": "LDSHack",
        "logo": "https://www.ldshack.org/img/logo.svg",
        "url": "https://ldshack.org",
        "contact": {
            "email": "info@ldshack.org",
        },
        "issue_report_channels": ["email"],
        "state": {
            "open": False,
            "message": "Work in progress"
        }
    }
