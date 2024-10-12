from flask import Flask
from app.routes import bp as routes_bp
from app.routes_front import bp as frontroutes_bp

#app
def create_app():
    app = Flask(__name__)

    app.register_blueprint(routes_bp)
    app.register_blueprint(frontroutes_bp)
    return app
