from flask import Flask
from dotenv import load_dotenv
import os
import json

load_dotenv()  # Cargar variables de entorno desde .env

def create_app():
    app = Flask(__name__)

    # Leer el contenido del JSON desde la variable de entorno
    credentials_json = os.getenv('GOOGLE_CREDENTIALS_JSON')
    if credentials_json:
        try:
            credentials_dict = json.loads(credentials_json)
            with open('google_credentials.json', 'w') as f:
                json.dump(credentials_dict, f)
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_credentials.json'
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
    else:
        print("GOOGLE_CREDENTIALS_JSON not found in environment variables")

    with app.app_context():
        from .routes import main
        app.register_blueprint(main)

    return app
