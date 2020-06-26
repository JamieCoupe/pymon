import webbrowser
from flask import Flask

app = Flask(__name__)
app.static_folder = 'static'

from app import routes


def open_page():
    print('opening page')
    webbrowser.open("http://127.0.0.1:5000/index", new=1)


#open_page()
