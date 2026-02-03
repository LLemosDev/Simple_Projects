from flask import Flask 

def register_routes(app: Flask):
    from .home import home_bp
    from .register import register_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(register_bp)