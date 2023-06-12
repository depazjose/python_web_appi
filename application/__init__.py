from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, template_folder = "templates")
    app.secret_key = 'h1h2h3h4h5h6h7h8'

    from . import urlshort
    app.register_blueprint(urlshort.bp)
    return app
