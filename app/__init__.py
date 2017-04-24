from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = "maybe"

from app import views,model

