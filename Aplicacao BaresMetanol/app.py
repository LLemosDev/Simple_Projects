from flask import Flask
from controller import register_routes
from models.db import db
import secrets
from config import Config

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{Config.passwordDB}@localhost/bd_agenda'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)