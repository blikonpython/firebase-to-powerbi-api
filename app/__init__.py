from flask import Flask
from dotenv import load_dotenv
import os
import json

load_dotenv()  # Cargar variables de entorno desde .env

def create_app():
    app = Flask(__name__)

    credentials_json = os.getenv('GOOGLE_CREDENTIALS_JSON')
    if credentials_json:
        with open('google_credentials.json', 'w') as f:
            f.write(credentials_json)
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_credentials.json'

    with app.app_context():
        from .routes import main
        app.register_blueprint(main)

    return app
