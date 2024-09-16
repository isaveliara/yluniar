from flask import Flask
from app.routes import bp as routes_bp

#app
def criar_app():
    app = Flask(__name__)

    app.register_blueprint(routes_bp)
    return app
