from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .routes import main
        app.register_blueprint(main)

    return app
