import os


class ConfigBase(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TITLE = "Flask Steam"
    THEME = os.environ.get('THEME','deep-purple')
    CACHE_TYPE= "SimpleCache"
    EXTENSIONS = [
        "flask_steam.ext.cache:init_app",
        "flask_steam.ext.database:init_app",
        "flask_steam.blueprints.favorite:init_app",
    ]
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI =  os.environ['DATABASE_URI']

class Config(ConfigBase):
    EXTENSIONS = [
        "flask_debugtoolbar:DebugToolbarExtension"
    ]
    TEMPLATES_AUTO_RELOAD = True
    DEBUG_TOOLBAR_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True
    DEBUG_TB_PANELS = [
        "flask_debugtoolbar.panels.versions.VersionDebugPanel",
        "flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel",
        "flask_debugtoolbar.panels.timer.TimerDebugPanel",
        "flask_debugtoolbar.panels.headers.HeaderDebugPanel",
        "flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel",
        "flask_debugtoolbar.panels.template.TemplateDebugPanel",
        "flask_debugtoolbar.panels.route_list.RouteListDebugPanel",
        "flask_debugtoolbar.panels.logger.LoggingPanel",
        "flask_debugtoolbar.panels.profiler.ProfilerDebugPanel",
        "flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel"
    ]


class ConfigTesting(ConfigBase):
    SECRET_KEY = "secret_testing"
    SQLALCHEMY_DATABASE_URI =  'sqlite:///test.sqlite3'