from flask import Flask

app = Flask(__name__)

from app import routes
import webbrowser

print('opening page')
webbrowser.open("http://127.0.0.1:5000/index", new=1)
