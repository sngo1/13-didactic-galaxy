from flask import Flask, render_template, redirect, url_for, request, session, flash
from utils import auth, edit, database


app = Flask(__name__)
app.secret_key = os.urandom(32)


# Login Authentication
@app.route('/')
def hello():
    return render_template('launch.html', test = "Hello World")

if __name__ == "__main__":
    app.debug = True
    app.run()
