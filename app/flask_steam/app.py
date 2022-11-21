from flask import Flask


def create_app(config_object='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    from ext.database import db, migrate
    from ext.cache import cache
    
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    
    register_blueprints(app)
    return app


def register_blueprints(app):
    from blueprints import favorite
    app.register_blueprint(favorite.favorite_bp)